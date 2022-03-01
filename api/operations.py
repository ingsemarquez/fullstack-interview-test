import os
import typing
import strawberry

#from git import Repo
from schemas import Author, Branch,  Commit, PullRequest

#print(os.getcwd())
#repo = Repo()
#assert not repo.bare

@strawberry.type
class Query:
    @strawberry.field
    def authors(self) -> typing.List[Author]:
        pass
    
    @strawberry.field
    def branches(self) -> typing.List[Branch]:
        pass
    
    @strawberry.field
    def commits(self) -> typing.List[Commit]:
        pass

    @strawberry.field
    def pull_request(self) -> typing.List[PullRequest]:
        pass


@strawberry.input
class AddPullRequest:
    title: str = strawberry.field(description="title of the Pull Request")
    description: str = strawberry.field(description="description of the Pull Request")
    status: str = strawberry.field(description="status of the Pull Request")
    author: 'Author' = strawberry.field(description="author of the Pull Request")
    origin: 'Branch' = strawberry.field(description="origin branch of the Pull Request")
    target: 'Branch' = strawberry.field(description="target branch of the Pull Request")


@strawberry.type
class Mutation:
    @strawberry.field
    def add_pull_request(self, pull_request: AddPullRequest) -> PullRequest:
        pass
