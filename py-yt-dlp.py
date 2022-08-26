from distutils.log import error
import os
import sys
import tkinter as tk
from tkinter import Canvas, filedialog, Text

def generateYTDLPcommand(*args):
    try:
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
            os.system('yt-dlp -x --audio-format m4a --paths "Downloads/" "'+YT_link+'"')
    except ValueError:
        pass

root = tk.Tk()
root.title("YT-DLP Command Generator")

canvas = tk.Canvas(root, height=500, width=500)
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
# window.grid(column=0, row=0, sticky=())
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
# frame.grid()

tk.Button(frame, text="Run Command", command="").grid(column=1,row=0)
root.mainloop()

# from tkinter import *
# from tkinter import ttk

# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass

# root = Tk()
# root.title("Feet to Meters")

# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# feet = StringVar()
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))

# meters = StringVar()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# for child in mainframe.winfo_children(): 
#     child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind("<Return>", calculate)

# root.mainloop()