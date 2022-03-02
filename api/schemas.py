from datetime import datetime
from typing import List
from enum import Enum


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

    def __init__(self, sha: str, message: str, author: Author, timestamp: datetime) -> None:
        self.sha = sha
        self.message = message
        self.author = author,
        self.timestamp = timestamp


class Branch:
    name: str
    commits: 'List[Commit]'

    def __init__(self, name: str) -> None:
        self.name = name


class PullRequest:
    title: str
    description: str
    status: 'Status'
    author: 'Author'
    origin: 'Branch'
    target: 'Branch'

    def __init__(self, title: str, description: str, status: Status, author: Author, origin: Branch, target: Branch) -> None:
        pass
