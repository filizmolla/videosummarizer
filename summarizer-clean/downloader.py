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
        self.id = None 
        self.title = None 
        self.ext = None 
        self.title_with_ext = None 
        self.description = None 
        self.channel_name = None 
        self.channel_url = None 
        self.upload_date_youtube = None
        self.duration = None 
        self.view_count = None 
        self.like_count = None 
        self.categories = None  
        self.tags = None 
        self.audio_path = None 
        self.subtitles = None 
        self.transcript = None
        self.transcript_path = None
        self.transcribing_start_date = None
        self.transcribing_end_date = None
        self.transcribing_time = None
        self.transcript_from = None
        self.transcript_word_count = None
        self.transcript_token_count = None
        self.transcript_character_count = None
        self.transcript_chunks = None
        self.transcript_embedding  = None
        self.date_uploaded = None
        self.download_start_datetime = None
        self.download_end_datetime = None
        self.download_time = None
        self.created_at = None
        self.updated_at = None
        self.is_summarized = None
        self.is_transcribed = None
        self.status  = None 
        self.playlist_id = None
        self.playlist_order = None
        self.is_in_playlist = None
        #self.summaries = None

    def __repr__(self) -> str:
        #return f"Video(id={self.id!r}, url={self.url!r}, title={self.title!r})"
        return f"""id= {self.id}
            url= {self.url}
            title= {self.title}
            ext= {self.ext}
            title_with_ext= {self.title_with_ext}
            description= {self.description}
            channel_name= {self.channel_name}
            channel_url= {self.channel_url}
            upload_date_youtube= {self.upload_date_youtube}
            duration= {self.duration}
            view_count= {self.view_count}
            like_count= {self.like_count}
            categories= {self.categories}
            tags= {self.tags}
            audio_path= {self.audio_path}
            subtitles= {self.subtitles}
            transcript= {self.transcript}
            transcript_path= {self.transcript_path}
            transcribing_start_date= {self.transcribing_start_date}
            transcribing_end_date= {self.transcribing_end_date}
            transcribing_time= {self.transcribing_time}
            transcript_from= {self.transcript_from}
            transcript_word_count= {self.transcript_word_count}
            transcript_token_count= {self.transcript_token_count}
            transcript_character_count= {self.transcript_character_count}
            transcript_chunks= {self.transcript_chunks}
            transcript_embedding= {self.transcript_embedding}
            date_uploaded= {self.date_uploaded}
            download_start_datetime= {self.download_start_datetime}
            download_end_datetime= {self.download_end_datetime}
            download_time= {self.download_time}
            created_at= {self.created_at}
            updated_at= {self.updated_at}
            is_summarized= {self.is_summarized}
            is_transcribed= {self.is_transcribed}
            status= {self.status}
            playlist_id= {self.playlist_id}
            playlist_order= {self.playlist_order}
            is_in_playlist= {self.is_in_playlist}"""
    
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
    videresult =    downloader.download_video()
    print(videresult)
