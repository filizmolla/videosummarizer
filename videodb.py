from models import Base, Video, Summary
from sqlalchemy import create_engine
from videosummarize import summarize
from videobatchsummarize import summarize_video_list
from sqlalchemy.orm import Session

db_user: str = 'postgres'
db_port: int = 5432
db_host: str= 'localhost'
db_password: str = 'postgres'
uri: str = F'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/summarizer'
SQLALCHEMY_DATABASE_URL = uri
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base.metadata.create_all(engine)

def add_videos_to_db(video_list):
    with Session(engine) as session:
        session.add_all(video_list)
        session.commit()

if __name__ == "__main__": 
    vl_str = """https://www.youtube.com/watch?v=X1CM3rZwGn8
    """
    vl = [Video(url=vid.strip()) for vid in vl_str.splitlines() if vid.strip()]
    summarize_video_list(vl)
    print(vl)
    add_videos_to_db(vl)
    