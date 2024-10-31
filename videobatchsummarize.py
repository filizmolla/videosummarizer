from videosummarizer import VideoSummarizer
from videotranscriber import VideoTranscriber
from models import Video
from videosummarize import summarize

def summarize_video_list(video_list):
    print(video_list)
    for video in video_list:
        summarize(video)
        
if __name__ == "__main__":    
    vl_str = """https://www.youtube.com/watch?v=orJSJGHjBLI
    """
    vl = [Video(url=vid.strip()) for vid in vl_str.splitlines() if vid.strip()]

    summarize_video_list(vl)