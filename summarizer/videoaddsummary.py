from models import Base, Video, Summary
from sqlalchemy import create_engine
from videobatchsummarize import summarize_video_list
from sqlalchemy.orm import Session
from videodb import engine
from videosummarize import summarize_video

def add_summary(id):
    with Session(engine) as session:
        v =session.get(Video, id) 
        s = summarize_video(v)
        v.summaries.append(s)
        print(v)
        print(s)
        session.add(s)
        session.commit()
    
if __name__ == "__main__": 
    input_id = 10
    add_summary(input_id)