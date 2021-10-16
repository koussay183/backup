import pafy
from tkinter import messagebox

def songdown(url,pathe):
      try:
        video = pafy.new(url)
        audiostreams = video.audiostreams
        bstaudio = video.getbestaudio()
        bstaudio.download(filepath = pathe)
        messagebox.showinfo('Download','Your Song Is Ready')
      except (KeyError,ValueError):
        messagebox.showerror('Error','This is not a youtube video')
def vediodown(url,linkentry,pathe):
    try :
        from pytube import YouTube
        from pytube import Playlist
    except Exception as e :
        print('Some Modules are Missing {}'.format(e))
    try :
        ytd = YouTube(url).streams.get_highest_resolution().download(output_path=pathe)
        messagebox.showinfo('Download','Your video is ready')
    except (KeyError,OSError):
        messagebox.showerror('Error','This is not a youtube video')
    finally :
        if linkentry.get() == '':
            messagebox.showerror("Error","Please enter a link")
