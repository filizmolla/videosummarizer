from __future__ import annotations

import re
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
        subtitles_path = PATH + "\\test videos\\output\\subtitles"

        def __init__(self, video: Video):
            self.video = video
            
        def start(self):
            self.download_video(self.video)

        def download_video(self, video: Video, languages=['tr', 'en']):
            ydl_opts = {
                'writesubtitles': True,             # Download subtitles
                'subtitleslangs': languages,        # Specify languages to download
                'subtitlesformat': 'vtt',           # Set subtitle format to .vtt
                'skip_download': False,              # Download the audio
                'format': 'm4a/bestaudio/best',
                'writeautomaticsub': False,         # Do not download auto-generated subtitles
                'outtmpl': {
                    'default': os.path.join(self.audio_download_directory, '%(title)s.%(ext)s'),    # Name for audio file
                    'subtitle': os.path.join(self.subtitles_path, '%(title)s.%(ext)s'),          # Name for subtitles file
                },
                'postprocessors': [
                {  # Extract audio using ffmpeg
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'm4a',
                },
                {# Postprocess to convert to .vtt if .srt is downloaded
                    'key': 'FFmpegSubtitlesConvertor',
                    'format': 'vtt',
                }],
                #'quiet': True,                      # Suppress output
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
                    start_time, end_time = self.format_time(start_time, end_time)

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
            
            def clean_subtitles(subtitle_text):
                """
                This function takes subtitle text as input, removes the timestamp numbers, the header line, and returns a continuous text.

                Parameters:
                subtitle_text (str): The raw subtitle text.

                Returns:
                str: The cleaned continuous text.
                """
                # Split the text into lines
                lines = subtitle_text.splitlines()
                
                # Remove the first line if it contains the header information
                if lines and 'WEBVTT' in lines[0]:
                    lines.pop(0)  # Remove the header line
                if 'Kind: captions' in lines[0]: 
                    lines.pop(0)
                if 'Language:' in lines[0]:
                    lines.pop(0)

                # Join the remaining lines into a single string
                cleaned_text = ' '.join(lines)

                # Regular expression to remove timestamps
                cleaned_text = re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}', '', cleaned_text)
                
                # Remove HTML entities like &nbsp;
                cleaned_text = re.sub(r'&nbsp;', ' ', cleaned_text)

                # Replace multiple spaces with a single space and strip leading/trailing spaces
                cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
                
                return cleaned_text
            start_time = time.time()    
            # if the video has human subtitles skip the transcribing part. 
            for lang in languages:
                subtitle_name = f"{video.title}.{lang}.vtt"
                subtitle_file = self.subtitles_path + "\\" + subtitle_name
                print(subtitle_file)
                if os.path.isfile(subtitle_file): # Find the subtitle file's path and check if it exists.
                    print("Exist")
                    with open(subtitle_file, 'r', encoding='utf-8') as f:
                        raw_subtitles = f.read().strip()
                        video.subtitles = raw_subtitles
                        transcript = clean_subtitles(raw_subtitles)
                        video.transcript = transcript     
                    self.save_transcript(video, video.transcript)
                    end_time = time.time()
                    transcribing_time = end_time - start_time
                    video.transcript_from = "from_subtitles"
                    start_time, end_time = self.format_time(start_time, end_time)
                    video.transcribing_start_date = start_time
                    video.transcribing_end_date = end_time 
                    video.transcribing_time = transcribing_time
                    return video
                else:
                    print(f"Video subtitles with {subtitle_file} does not exist.")
            print("Video does not have subtitles with the languages selected!")
            self.transcribe_video(self.video)
            return video
        




        def format_time(self, start_time, end_time):
            start_time_str = strftime('%Y-%m-%d %H:%M:%S', localtime(start_time))
            start_time = PyDateTime.strptime(start_time_str, '%Y-%m-%d  %H:%M:%S')
            end_time_str = strftime('%Y-%m-%d %H:%M:%S', localtime(end_time))
            end_time = PyDateTime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
            return start_time, end_time

        def save_transcript(self, video: Video, transcript_text):
            transcript_path = self.transcripts_path + "\\" + video.title +".txt"
            video.transcript = transcript_text
            video.transcript_path = transcript_path
            video.is_transcribed = True
            video.status = "Transcribed."
            with open(transcript_path, "w", encoding="utf-8") as file: 
                file.write(transcript_text)
            print(f"\nTranscript is saved to {transcript_path}")

        def transcribe_video(self, video: Video):
            print("\n-------------")
            print(video.title_with_ext)
            start_time = time.time()
            model = whisper.load_model("base")
            result = model.transcribe(self.audio_download_directory + "\\" + video.title_with_ext)
            transcript_text = result['text']
            end_time = time.time() 
            transcribing_time = end_time - start_time
            print(f"\nTranscribing completed in {transcribing_time:.2f} seconds.")
            start_time, end_time = self.format_time(start_time, end_time)
            video.transcribing_start_date = start_time
            video.transcribing_end_date = end_time 
            video.transcribing_time = transcribing_time
            self.save_transcript(video, transcript_text)
            video.transcript_from = "whisper"
            return transcript_text
        
        