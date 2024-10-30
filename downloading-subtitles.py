import yt_dlp
import re 
import os 

def clean_subtitles(subtitle_text):
    """
    This function takes subtitle text as input, removes the timestamp numbers,
    the header line, and returns a continuous text.

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


def download_human_subtitles(video_url, languages=['en', 'tr']):
    """
    Download human-generated subtitles from a YouTube video and return the cleaned text.

    Parameters:
    video_url (str): The URL of the YouTube video.
    languages (list): List of languages for the subtitles to download.

    Returns:
    str: The cleaned continuous subtitle text.
    """
    ydl_opts = {
        'writesubtitles': True,             # Download subtitles
        'subtitleslangs': languages,        # Specify languages to download
        'subtitlesformat': 'vtt',           # Set subtitle format to .vtt
        'skip_download': False,              # Download the audio
        'format': 'm4a/bestaudio/best',
        'writeautomaticsub': False,         # Do not download auto-generated subtitles
        'outtmpl': {
            'default': 'audio_downloaded.%(ext)s',    # Name for audio file
            'subtitle':  '%(title)s.%(ext)s',          # Name for subtitles file
        },
        'postprocessors': [
        {  # Extract audio using ffmpeg
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'm4a',
        },
        {                 # Postprocess to convert to .srt if .vtt is downloaded
            'key': 'FFmpegSubtitlesConvertor',
            'format': 'vtt',
        },
        ],
        #'quiet': True,                      # Suppress output
    }

    print(ydl_opts['outtmpl'])

    # Variable to hold the subtitle file name
    subtitle_file = None

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
        info_dict = ydl.extract_info(video_url, download=False)
        video_id = info_dict['id']
        video_title = info_dict['title']

        
        for lang in languages:
            subtitle_file = f"{video_title}.{lang}.vtt"
            print(subtitle_file)
            if os.path.isfile(subtitle_file): # Find the subtitle file's path and check if it exists.
                print("Exist")
                with open(subtitle_file, 'r', encoding='utf-8') as f:
                    raw_subtitles = f.read().strip()
                    return clean_subtitles(raw_subtitles)
            else:
                print(f"Video subtitles with {subtitle_file} does not exist.")
        print("Video does not have subtitles with the languages selected!")
        return ""
 

# Kullanım örneği
video_url = "https://www.youtube.com/watch?v=OTNe0eV8418"
subtitles = download_human_subtitles(video_url, languages=['tr', 'en'])
print(subtitles)