import typing
import strawberry

from enum import Enum


@strawberry.enum
class Status(Enum):
    Open = 'Open'
    Closed = 'Closed'
    Merged = 'Merged'


@strawberry.type
class Author:
    name: str
    email: str


@strawberry.type
class Commit:
    sha: str
    message: str
    author: 'Author'
    timestamp: str


@strawberry.type
class Branch:
    name: str
    commits: typing.List['Commit']


@strawberry.type
class PullRequest:
    title: str
    description: str
    status: 'Status'
    author: 'Author'
    origin: 'Branch'
    target: 'Branch'
