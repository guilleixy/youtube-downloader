import yt_dlp

url = input("Enter the YouTube video URL: ")

ydl_opts = {
    "format": "bestvideo+bestaudio/best",
    "merge_output_format": "mp4",
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
