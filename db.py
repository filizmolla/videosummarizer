from models import Base, Video, Summary
from sqlalchemy import create_engine
from videosummarize import summarize

db_user: str = 'postgres'
db_port: int = 5432
db_host: str= 'localhost'
db_password: str = 'postgres'
uri: str = F'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/summarizer'
SQLALCHEMY_DATABASE_URL = uri
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base.metadata.create_all(engine)

from sqlalchemy.orm import Session
with Session(engine) as session:
    v = Video(url="https://www.youtube.com/watch?v=ITwW825L4zg")
    summarize(v)
    session.add_all([v])

    session.commit()
