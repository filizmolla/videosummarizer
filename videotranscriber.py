from __future__ import annotations

import asyncio
import whisper
import yt_dlp
import os 
import time 
from time import localtime, strftime
from datetime import datetime as PyDateTime
from models import Video

class VideoTranscriber: 
        PATH = os.getcwd()
        audio_download_directory = PATH + "\\test videos\\output\\audios"
        transcripts_path = PATH + "\\test videos\\output\\transcripts"

        def __init__(self, video: Video):
            self.video = video
            
        def start(self):
            self.download_video(self.video)
            self.transcribe_video(self.video)

        def download_video(self, video: Video):
            ydl_opts = {
                'outtmpl': os.path.join(self.audio_download_directory, '%(title)s.%(ext)s'),
                'format': 'm4a/bestaudio/best',
                'postprocessors': [{  # Extract audio using ffmpeg
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'm4a',
                }]
            }

            print(ydl_opts['outtmpl'])
            url = video.url

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

                    video.title = title 
                    video.ext = ext
                    video.title_with_ext = title_with_ext
                    video.channel_name = uploader 
                    video.upload_date_youtube = PyDateTime.strptime(upload_date_str, '%Y%m%d')
                    video.description = description
                    video.duration = duration
                    video.view_count = view_count 
                    video.like_count = like_count
                    video.channel_url = channel_url 
                    video.categories = ', '.join(categories) # Convert list to string
                    video.tags = ', '.join(tags) # convert list to string
                    video.audio_path = self.audio_download_directory + "\\" + title_with_ext

                    start_time = time.time()
                    print(f'Downloading: {url}')
                    ydl.download([url])
                    end_time = time.time() 
                    download_time = end_time - start_time
                    print(f"Download completed in {download_time:.2f} seconds.")
                    start_time_str = strftime('%Y-%m-%d %H:%M:%S', localtime(start_time))
                    start_time = PyDateTime.strptime(start_time_str, '%Y-%m-%d  %H:%M:%S')
                    end_time_str = strftime('%Y-%m-%d %H:%M:%S', localtime(end_time))
                    end_time = PyDateTime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')

                    video.download_start_datetime = start_time
                    video.download_end_datetime = end_time 
                    video.download_time = download_time

                    print("---------------\n")
                    print(f"Download start time {video.download_start_datetime}" )
                    print(f"Download end time {video.download_end_datetime}" )
                    print(f"Download time {video.download_time}" )
                    print("\n--------------------")
                    
                    video.status = "Downloaded."
                except Exception as e: 
                    print(f'Failed to download {url}. Error: {e}')
                    video.status = "Download failed."
            print(f"After Download metod Url={url}, title_with_ext: {title_with_ext}")
            return video

        def transcribe_video(self, video: Video):
            print("\n-------------")
            print(video.title_with_ext)
            start_time = time.time()
            model = whisper.load_model("base")
            result = model.transcribe(self.audio_download_directory + "\\" + video.title_with_ext)
            transcript_text = result['text']
            end_time = time.time() 
            download_time = end_time - start_time
            print(f"\nTranscribing completed in {download_time:.2f} seconds.")
            start_time_str = strftime('%Y-%m-%d %H:%M:%S', localtime(start_time))
            start_time = PyDateTime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
            end_time_str = strftime('%Y-%m-%d %H:%M:%S', localtime(end_time))
            end_time= PyDateTime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')


            video.transcribing_start_date = start_time
            video.transcribing_end_date = end_time 
            video.transcribing_time = download_time

            transcript_path = self.transcripts_path + "\\" + video.title +".txt"

            video.transcript = transcript_text
            video.transcript_path = transcript_path
            video.is_transcribed = True
            video.status = "Transcribed."
        
            with open(transcript_path, "w", encoding="utf-8") as file: 
                file.write(transcript_text)
            print(f"\nTranscript is saved to {transcript_path}")
            return transcript_text
        