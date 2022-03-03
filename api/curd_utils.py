from pydoc import describe
from typing import List, Optional
from models import PullRequestModel
from schemas import PullRequest
from sqlalchemy.orm import Session


class PullRequestCrud:
    def add(self, db: Session, pr: PullRequest) -> PullRequestModel:
        db_pr = PullRequestModel(
            title=pr.title,
            description=pr.description,
            status=pr.status,
            author=pr.author,
            origin=pr.origin,
            target=pr.target
        )
        db.add(db_pr)
        db.commit()
        db.refresh(db_pr)
        return db_pr
    
    def update(self, db: Session, pr: PullRequestModel):
        db.update(pr)
        db.commit()

    def get(self, db: Session):
        return db.query(PullRequestModel) \
                .order_by(PullRequestModel.timestamp.desc()) \
                .all()