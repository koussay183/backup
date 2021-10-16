import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
bg = '#7F00FF'  #FF0000
fnt = 'impact',40
def down():
    try :
        from pytube import YouTube
        from pytube import Playlist
    except Exception as e :
        print('Some Modules are Missing {}'.format(e))
    try :
        url = link.get()
        ytd = YouTube(url).streams.first().download()
        messagebox.showinfo('Download','Your video is ready')
    except KeyError :
        messagebox.showerror('Error','This is not a youtube video')

frm = tkinter.Tk()
frm.title('Download-Manager')
frm.geometry('800x305+300+200')
frm.resizable(False,False)
photo = PhotoImage(file = "logo.png")
frm.iconphoto(False, photo)
frm.config(background = bg)

btns = ttk.Style()
btns.configure('TButton',font =fnt,background=bg,highlightcolor='#7F00FF')

lbl1 = Label(frm,text='-- Enter link to Download --',font=fnt,background='#FF1493',foreground='black',relief='solid',bd=4,padx=10,pady=10)
link = Entry(frm,font=('tahoma',30),relief='solid',bd =4)
#dbtn = ttk.Button(frm,style='TButton',text='Download',command=down)
dbtn = Button(frm,bg = '#FF1493',text='Download',command=down,font=('impact',30),activebackground='#FF1493',bd=3)

lbl1.grid(row=0,column=0,pady=5,padx=110)
link.grid(row=1,column=0,pady=20,padx=110)
dbtn.grid(row=2,column=0,pady=10,padx=110)


frm.mainloop()
