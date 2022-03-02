import os
import strawberry


from typing import List, Optional
from git import Repo
from schemas import Author, Branch,  Commit, PullRequest


#repo = Repo(os.getcwd(), search_parent_directories=True)
#print(repo.git.branch('-r'))
#print('comence')
#assert not repo.bare

@strawberry.type
class Query:
    @strawberry.field
    def authors(self) -> Optional[List[Author]]:
        pass
    
    @strawberry.field
    def branches(self) -> Optional[List[Branch]]:
        #branch_list = []
        #print(repo.git.branch('-r').split('\n'))
        #for branch_name in repo.git.branch('-r').split('\n'):
        #    print(branch_name)
        #    list.append(Branch(branch_name))
        #return branch_list
        pass
    
    @strawberry.field
    def commits(self, branch_name: str) -> Optional[List[Commit]]:
        pass

    @strawberry.field
    def pull_request(self) -> Optional[List[PullRequest]]:
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
