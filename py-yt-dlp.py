import os

dl_format = input("What format do you want to download in? Options are: audio, video\n")

# audio downloads
if (dl_format == "audio" or "a"):
    audio_format = input("What audio format?\n")

    if (audio_format == "3" or "MP3"):
        audio_format = "mp3"

# video downloads
else:
    print("you suck\n")
    exit()

YT_link = input("Paste the YouTube link\n")

home_dir = os.system('yt-dlp -x --audio-format '+audio_format+' "'+YT_link+'"')
