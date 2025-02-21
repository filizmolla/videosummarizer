from __future__ import annotations
from models import LLMModel, GemineModel, ChatGPTModel
import os 
import time
import json
from time import localtime, strftime
from datetime import datetime as PyDateTime
import yt_dlp


class VideoResult:
    
    def __init__(self, url: str):
        self.url= url
        self.id = None # Mapped[int] = mapped_column(primary_key=True)
        self.title = None # Mapped[Optional[str]]    
        self.ext = None # Mapped[Optional[str]]
        self.title_with_ext = None # Mapped[Optional[str]]
        self.description = None # Mapped[Optional[str]]
        self.channel_name = None # Mapped[Optional[str]]
        self.channel_url = None # Mapped[Optional[str]]
        self.upload_date_youtube = None # Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
        self.duration = None # Mapped[Optional[int]]
        self.view_count = None # Mapped[Optional[int]]
        self.like_count = None # Mapped[Optional[int]]
        self.categories = None # Mapped[Optional[str]] 
        self.tags = None # Mapped[Optional[str]]
        self.audio_path = None # Mapped[Optional[str]]
        self.subtitles = None # Mapped[Optional[str]] = mapped_column(Text, nullable=True) # long string
        self.transcript = None# Mapped[Optional[str]] = mapped_column(Text, nullable=True)  # can hold arbitrarily long string
        self.transcript_path = None# Mapped[Optional[str]] 
        self.transcribing_start_date = None# Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
        self.transcribing_end_date = None# Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
        self.transcribing_time = None# Mapped[Optional[int]]
        self.transcript_from = None# Mapped[Optional[str]]
        self.transcript_word_count = None# Mapped[Optional[int]]
        self.transcript_token_count = None# Mapped[Optional[int]]
        self.transcript_character_count = None# Mapped[Optional[int]]
        self.transcript_chunks = None# Mapped[Optional[str]]
        self.transcript_embedding  = None# mapped_column(Vector(1536))
        self.date_uploaded = None# Mapped[Optional[DateTime]] =  mapped_column(DateTime, nullable=True)
        self.download_start_datetime = None# Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
        self.download_end_datetime = None# Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
        self.download_time = None# Mapped[Optional[int]]
        self.created_at = None# Mapped[Optional[DateTime]] = mapped_column(DateTime, default=func.now(), nullable=False)
        self.updated_at = None# Mapped[Optional[DateTime]] = mapped_column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
        self.is_summarized = None# Mapped[Optional[Boolean]] = mapped_column(Boolean, default=False)
        self.is_transcribed = None# Mapped[Optional[Boolean]] = mapped_column(Boolean, default=False)
        self.status  = None# Mapped[Optional[str]] = mapped_column(default="Pending.") # Pending / Done 
        self.playlist_id = None# Mapped[Optional[str]]
        self.playlist_order = None# Mapped[Optional[int]]
        self.is_in_playlist = None# Mapped[Optional[Boolean]]= mapped_column(Boolean, default=False)
        #self.summaries = None# Mapped[List["Summary"]] = relationship(back_populates="video", cascade="all, delete-orphan", lazy='select')

    def __repr__(self) -> str:
        return f"Video(id={self.id!r}, url={self.url!r}, title={self.title!r})"

class TimeFormatter:

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time 

    def format_time(self):
        start_time_str = strftime('%Y-%m-%d %H:%M:%S', localtime(self.start_time))
        start_time = PyDateTime.strptime(start_time_str, '%Y-%m-%d  %H:%M:%S')
        end_time_str = strftime('%Y-%m-%d %H:%M:%S', localtime(self.end_time))
        end_time = PyDateTime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
        return start_time, end_time
 
class VideoDownloader: 
    PATH = "C:\\workdir\\pkm\\summarizer\\test videos\\output\\"
    audio_download_directory = PATH + "audios"
    subtitles_path = PATH + "subtitles"

    def __init__(self, videoresult: VideoResult):
        self.videoresult = videoresult

    def download_video(self, languages=['tr', 'en']):
        ydl_opts = {
            'writesubtitles': True,             # Download subtitles
            'subtitleslangs': languages,        # Specify languages to download
            'subtitlesformat': 'vtt',           # Set subtitle format to .vtt
            'skip_download': False,             # Download the audio
            'format': 'm4a/bestaudio/best',
            'writeautomaticsub': False,         # Do not download auto-generated subtitles
            'outtmpl': {
                'default': os.path.join(self.audio_download_directory, '%(title)s.%(ext)s'),    # Name for audio file
                'subtitle': os.path.join(self.subtitles_path, '%(title)s.%(ext)s'),          # Name for subtitles file
            },
            'postprocessors': [
            {   
                # Extract audio using ffmpeg
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            },
            {   
                # Postprocess to convert to .vtt if .srt is downloaded
                'key': 'FFmpegSubtitlesConvertor',
                'format': 'vtt',
            }],
            #'quiet': True, # Suppress output
        }

        print(ydl_opts['outtmpl'])
        url = self.videoresult.url

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                info_dict = ydl.extract_info(url, download=False)

                downloaded_filename = ydl.prepare_filename(info_dict)

                title, ext = os.path.splitext(os.path.basename(downloaded_filename)) # (title)(.ext)
                title_with_ext = f"{title}{ext}" 
                ext = ext[1:] # Exclude the dot.                   
                uploader = info_dict.get('uploader', 'Unknown uploader')
                upload_date_str = info_dict.get('upload_date', 'Unknown date')
                description = info_dict.get('description', 'No description available')
                duration = info_dict.get('duration', 0)
                view_count = info_dict.get('view_count', 0)
                like_count = info_dict.get('like_count', 'Unknown likes')
                channel_url = info_dict.get('channel_url', 'Unknown channel URL')
                categories = info_dict.get('categories', [])
                tags = info_dict.get('tags', [])

                self.videoresult.title = title 
                self.videoresult.ext = ext
                self.videoresult.title_with_ext = title_with_ext
                self.videoresult.channel_name = uploader 
                self.videoresult.upload_date_youtube = PyDateTime.strptime(upload_date_str, '%Y%m%d')
                self.videoresult.description = description
                self.videoresult.duration = duration
                self.videoresult.view_count = view_count 
                self.videoresult.like_count = like_count
                self.videoresult.channel_url = channel_url 
                self.videoresult.categories = ', '.join(categories) # Convert list to string
                self.videoresult.tags = ', '.join(tags) # convert list to string
                self.videoresult.audio_path = self.audio_download_directory + "\\" + title_with_ext

                start_time = time.time()
                print(f'Downloading: {url}')
                ydl.download([url])
                end_time = time.time() 
                download_time = end_time - start_time
                print(f"Download completed in {download_time:.2f} seconds.")

                formatter = TimeFormatter(start_time=start_time, end_time=end_time)
                start_time, end_time = formatter.format_time()

                self.videoresult.download_start_datetime = start_time
                self.videoresult.download_end_datetime = end_time 
                self.videoresult.download_time = download_time

                print("---------------\n")
                print(f"Download start time {self.videoresult.download_start_datetime}" )
                print(f"Download end time {self.videoresult.download_end_datetime}" )
                print(f"Download time {self.videoresult.download_time}" )
                print("\n--------------------")
                
                self.videoresult.status = "Downloaded."
            except Exception as e: 
                print(f'Failed to download {url}. Error: {e}')
                self.videoresult.status = "Download failed."
        print(f"After Download Method Url={url}, title_with_ext: {title_with_ext}")
        return self.videoresult
    

if __name__ == "__main__":
    video = VideoResult("https://www.youtube.com/watch?v=QspjKVTMlL8")
    downloader = VideoDownloader(video)
    downloader.download_video()

