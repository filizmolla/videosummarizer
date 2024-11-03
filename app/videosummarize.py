from videosummarizer import VideoSummarizer
from videotranscriber import VideoTranscriber
from models import Video

def transcribe_video(video):
    transcriber = VideoTranscriber(video)
    transcriber.start()

def summarize_video(video):
    summarizer=VideoSummarizer(video)
    s = summarizer.start()
    return s

def summarize(video):
    transcribe_video(video)
    summarize_video(video)

if __name__ == "__main__":    
    v = Video(url="https://www.youtube.com/watch?v=aAy-B6KPld8")
    summarize(v)
    print(v)
    for field, value in v.__dict__.items():
        print(f"{field}: {value}")
