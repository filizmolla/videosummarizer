from fastapi import Request, HTTPException, Depends
from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session, sessionmaker
from models import Video
import uvicorn
from videosummarize import summarize
from videodb import add_videos_to_db, engine

app = FastAPI()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/notify_new_data")
async def notify_new_data(request: Request, db: Session = Depends(get_db)):
    print("New record has been added to the database!")
    data = await request.json()
    
    print(data)
    video_url = data.get("url")
    print(video_url)

    #v = Video(url=video_url)
    #summarize(v)
    #add_videos_to_db([v])

    if not video_url:
        return JSONResponse(content={"message": "Record URL not provided"}, status_code=400)
    
    video = db.query(Video).filter(Video.url == video_url, Video.is_summarized == False).first()
    if video:
        summarize(video)
        db.commit()
        db.refresh(video)

        return JSONResponse(content={"message": "Video has been summarized and updated"}, status_code=200)
    else:
        raise HTTPException(status_code=404, detail="Video not found or already summarized")




if __name__ == "__main__":
    uvicorn.run("videoapi:app", host="127.0.0.1", port=5000, reload=True)
