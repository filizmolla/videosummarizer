from videosummarizer import VideoSummarizer
from videotranscriber import VideoTranscriber
from models import Video

def summarize(video):
    transcriber = VideoTranscriber(video)
    transcriber.start()

    summarizer=VideoSummarizer(video)
    summarizer.start()

if __name__ == "__main__":    
    v = Video(url="https://www.youtube.com/watch?v=K56nNuBEd0c")
    summarize(v)
    print(v)
    for field, value in v.__dict__.items():
        print(f"{field}: {value}")
