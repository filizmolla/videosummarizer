from videosummarizer import VideoSummarizer
from videotranscriber import VideoTranscriber
from models import Video

def summarize(video):
    transcriber = VideoTranscriber(video)
    transcriber.start()

    summarizer=VideoSummarizer(video)
    summarizer.start()

v = Video(url="https://www.youtube.com/watch?v=XsuouINoR1M")
summarize(v)
