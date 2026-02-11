import yt_dlp

url = input("Enter the YouTube video URL: ")

ydl_opts = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
    "merge_output_format": "mp4",
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
