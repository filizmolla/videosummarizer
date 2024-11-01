from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import JSONResponse
from models import Video
import uvicorn
from videosummarize import summarize
app = FastAPI()


# get one video
@app.post("/notify_new_data")
async def notify_new_data(request: Request):
    print("New record has been added to the database!")
    data = await request.json()
    
    print(data)
    video_url = data.get("url")
    print(video_url)
    v = Video(url=video_url)
    summarize(v)
    
    if not video_url:
        return JSONResponse(content={"message": "Record URL not provided"}, status_code=400)
    
if __name__ == "__main__":
    uvicorn.run("videoapi:app", host="127.0.0.1", port=5000, reload=True)
