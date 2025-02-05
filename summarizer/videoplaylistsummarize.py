import re 
import yt_dlp
from videobatchsummarize import summarize_video_list
from models import Video
from videodb import add_videos_to_db

def get_playlist_id(url):
    # Use regex to find the playlist ID
    match = re.search(r'(?:list=|playlist\?list=)([^&]+)', url)
    if match:
        return match.group(1)
    return None

def get_playlist_videos(playlist_id):
    playlist_url = f'https://www.youtube.com/playlist?list={playlist_id}'
    
    # Set yt-dlp options
    ydl_opts = {
        'extract_flat': True,  # Extract metadata without downloading videos
        'quiet': True          # Suppress yt-dlp output
    }
    
    # Use yt-dlp to fetch playlist info
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
    
    # Extract and return video details if it's a playlist
    if 'entries' in info:
        videos = []
        for video in info['entries']:
            videos.append({
                'title': video.get('title'),
                'url': f"https://www.youtube.com/watch?v={video.get('id')}"
            })
        return videos
    else:
        print("The provided URL is not a playlist.")
        return []

def get_videos_from_url(url):
    # Extract the playlist ID from the given URL
    playlist_id = get_playlist_id(url)
    
    if playlist_id:
        return get_playlist_videos(playlist_id)
    else:
        print("No valid playlist ID found in the URL.")
        return []

def get_video_list_formatted_from_url(playlist_url):
    videos = get_videos_from_url(playlist_url)
    vl_str = []
    for video in videos:
        print(f"Title: {video['title']}, URL: {video['url']}")
        vl_str.append(video['url'])

    vl = [Video(url=vid.strip()) for vid in vl_str]
    for i, v in enumerate(vl): 
        v.playlist_id = get_playlist_id(playlist_url)
        v.is_in_playlist = True
        v.playlist_order = i
        print(v)
        print(v.playlist_id)
        print(v.playlist_order)
        print(v.is_in_playlist)
    return vl

def summarize_playlist(playlist_url):
    vl = get_video_list_formatted_from_url(playlist_url)
    summarize_video_list(vl)
    add_videos_to_db(vl)

if __name__ == "__main__":
    url = 'https://www.youtube.com/watch?v=mRMmlo_Uqcs&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp'
    summarize_playlist(url)
