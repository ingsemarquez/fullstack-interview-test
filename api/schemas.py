from datetime import datetime
from typing import List
from enum import Enum
from pydantic import BaseModel


class Status(Enum):
    Open = 'Open'
    Closed = 'Closed'
    Merged = 'Merged'


class Author:
    name: str
    email: str

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email


class Commit:
    sha: str
    message: str
    author: 'Author'
    timestamp: datetime

    def __init__(self,
        sha: str,
        message: str,
        author: Author,
        timestamp: datetime
    ) -> None:
        self.sha = sha
        self.message = message
        self.author = author,
        self.timestamp = timestamp


class Branch:
    name: str
    commits: 'List[Commit]'

    def __init__(self, name: str) -> None:
        self.name = name


class PullRequest(BaseModel):
    title: str
    description: str
    status: 'Status'
    author: str
    origin: str
    target: str
    timestamp: datetime

    #def __init__(
    #    self, 
    #    title: str,
    #    description: str,
    #    status: Status,
    #    author: str,
    #    origin: str,
    #    target: str,
    #    timestamp: datetime
    #) -> None:
    #    self.title = title
    #    self.description = description
    #    self.status = status
    #    self.author = author
    #    self.origin = origin
    #    self.target = target
    #    self.timestamp = timestamp
    
    #class Config:
    #    orm_mode = True
