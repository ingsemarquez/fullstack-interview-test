from ast import If
import os
#import strawberry

from fastapi import FastAPI
#from strawberry.fastapi import GraphQLRouter
#from operations import Query
from git import Repo
from typing import List, Optional
from schemas import Author, Branch, Commit, PullRequest

# experiment with graphql
#schema = strawberry.Schema(Query)
#graphql_app = GraphQLRouter(schema)

app = FastAPI()

# old fashion way to do
repo = Repo(os.getcwd(), search_parent_directories=True)
assert not repo.bare

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
async def get_pull_request() -> Optional[List[str]]:
    prs = []
    for branch_name in repo.heads:
        prs.append(branch_name.name)
    return prs


#app.include_router(graphql_app, prefix='/graphql')