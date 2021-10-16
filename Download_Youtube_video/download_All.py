from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pafy

m = ('C:\\Users\\koussqy\\Desktop\\work\\2TI\\Download_Youtube_video\\Songs')


bgd = '#2E2939'  
fnt = 'impact',30
clr = 'black'
#=============================================================================================================================
frm = Tk()

frm.title('Download-Manager')
frm.geometry('800x395+300+200')
frm.resizable(False,False)
frm.config(background = bgd)

v = IntVar()
sv = StringVar()

photo = PhotoImage(file = "logo.png")
frm.iconphoto(False, photo)

lbl1 = ttk.Label(frm,text='- Enter Link To Download -')
lbl1.config(background = '#60efff' ,foreground = clr,font = ('impact',40),padding = (50,5))
link = Entry(frm,font = ('tahoma',30),textvariable=sv,relief='solid',bd=4)
cb2 =  Checkbutton(frm,text='Video + Audio',bg = "#60efff",fg = clr,font=('tahoma',13),variable=v,activebackground='#60efff')

#def===========================================================================================================================


def dff():
    
    if v.get() == 0 :
      try:  
        url = link.get()
        video = pafy.new(url)
        audiostreams = video.audiostreams
        bstaudio = video.getbestaudio()
        bstaudio.download(filepath = m)
        messagebox.showinfo('Download','Your Song Is Ready')
        sv.set('')
      except (KeyError,ValueError):
        messagebox.showerror('Error','This is not a youtube video')
        sv.set('')
    else :
        try :
            from pytube import YouTube
            from pytube import Playlist
        except Exception as e :
            print('Some Modules are Missing {}'.format(e))
        try :
            url = link.get()
            ytd = YouTube(url).streams.first().download()
            messagebox.showinfo('Download','Your video is ready')
            sv.set('')
        except (KeyError,OSError):
            messagebox.showerror('Error','This is not a youtube video')
            sv.set('')
        finally :
            if link.get() == '':
                messagebox.showerror("Error","Please enter a link")
#==============================================================================================================================

dbtn = Button(frm,text ='Download',command=dff,background='#60efff',foreground=clr,font=fnt,activebackground='#60efff')




lbl1.grid(row=0,column=0,padx=80,pady=7)
link.grid(row=1,column=0,pady=50)
dbtn.grid(row=2,column=0)
cb2.grid(row=3,column=0,pady=20)


frm.mainloop()
