import os

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from git import Repo
from typing import List, Optional
from schemas import Author, Branch, Commit, PullRequest
from models import Base, engine, db_session, PullRequestModel
from curd_utils import PullRequestCrud

# experiment with graphql using strawberry
#schema = strawberry.Schema(Query)
#graphql_app = GraphQLRouter(schema)

Base.metadata.create_all(engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()

# old fashion way to do
repo = Repo(os.getcwd(), search_parent_directories=True)
assert not repo.bare

crud = PullRequestCrud()

@app.get('/branches')
async def get_branches() -> Optional[List[Branch]]:
    branches = []
    for branch in repo.heads:
        branches.append(Branch(branch.name))
    return branches

@app.get('/commits_by_branch/{branch}')
async def get_commits(branch: str) -> Optional[List[Commit]]:
    commits = []
    commits_to_add = list(repo.iter_commits(branch))
    if len(commits_to_add) > 0:
        for commit in commits_to_add:
            commits.append(Commit(
                commit.hexsha,
                commit.message,
                Author(commit.author.name, commit.author.email),
                commit.committed_datetime))
    return commits

@app.get('/commit_detail/{sha}')
async def get_commit_detail(sha: str) -> Optional[Commit]:
    commit = repo.commit(sha)
    if commit is not None:
        return Commit(
            commit.hexsha,
            commit.message,
            Author(commit.author.name, commit.author.email),
            commit.committed_datetime)
    else:
        return None

@app.get('/pull_request')
async def get_pull_request(db: Session = Depends(get_db)) -> Optional[List[PullRequest]]:
    pull_requests = []
    try:
        pull_requests = crud.get(db)
    except:
        print('unhandled db failure')

    return pull_requests


@app.post('/pull_request')
async def add_pull_request(pull_request: PullRequest, db: Session = Depends(get_db)) -> Optional[PullRequest]:
    try:
        return crud.add(db=db, pr=pull_request)
    except:
        print('unhandled creation failure')
