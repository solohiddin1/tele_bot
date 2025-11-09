import yt_dlp

from config.log import setup_logger
import re

logger = setup_logger()

def sanitize(title):
    return re.sub(r'[\\/*?:"<>|｜%]', "", title)

ydl_options = {
    'format': 'bestaudio/best',
    'outtmpl': 'audios/%(title)s.%(ext)s',
    'max_file_size':100*1024*1024,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '64',  # low quality
    }],
    'no_sleep_requests':True,
}

opts = {"simulate":True}

def check_file_size(url,max_size=100*1024*1024):
    with yt_dlp.YoutubeDL(opts)as yt:
        info = yt.extract_info(url,download=False)
        size = info.get("filesize") or info.get("filesize_approx") or 0
        logger.info(f"File size  - > {size} bytes")
        return size <= max_size

def download_video(url):
    try:
        with yt_dlp.YoutubeDL(ydl_options)as y:
            info = y.extract_info(url,download=False)
            clean_title = sanitize(info.get("title","audio"))
            ydl_opts = {**ydl_options,'outtmpl': f"audios/{clean_title}.%(ext)s"}
            # file_name = y.prepare_filename(info).replace(".webm",".mp3")
            with yt_dlp.YoutubeDL(ydl_opts)as y2:
                y2.download(url)
            # file_name = f"audios/{clean_title}.mp3"
            return f"audios/{clean_title}.mp3"
    except yt_dlp.DownloadError as d:
        if "File is larger than max-filesize" in str(d):
            return "too_big"
        raise
# download_video("https://youtu.be/5T97A6xA-sc?si=KNBcb8CEHdnzN1GY")