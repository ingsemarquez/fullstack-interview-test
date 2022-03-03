from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Enum
from schemas import Status


Base = declarative_base()


engine = create_engine(
    'sqlite:///{}.sqlite'.format('pr_db'),
    connect_args={"check_same_thread": False}
)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class PullRequestModel(Base):
    __tablename__ = "pr_data"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(Enum(Status))
    author = Column(String)
    origin = Column(String)
    target = Column(String)
    timestamp = Column(DateTime)


    #def __init__(self) -> None:
    #    self.timestamp = current_timestamp()
