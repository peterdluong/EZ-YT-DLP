from distutils.log import error
import os
import sys

dl_format = input("What format do you want to download in? Options are: audio, video\n").lower()

# audio downloads
if (dl_format == "audio" or "a"):
    audio_format = input("What audio format?\n").lower()
    if (audio_format == "3" or "mp3"):
        audio_format = "mp3"
# video downloads
elif (dl_format == "video" or "v"):
    error("you suck\n")
    exit()

YT_link = input("Paste the YouTube link\n")

# different command depending on operating system
if sys.platform == 'win32':
    os.system('cd C:\ytdl')
    os.system('yt-dlp -x --audio-format '+audio_format+' --paths "Downloads/" "'+YT_link+'"')
elif sys.platform == 'darwin':
    print('hi')