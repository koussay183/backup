from tkinter import*
import tkinter
from tkinter import messagebox
from tkinter import ttk
import pafy
from random import *
import random
import time
import win32com.client as w 
import time as tm
import datetime
from PIL import Image,ImageTk
dt = datetime.datetime.now()
bgd = '#2E2939'  
fnt = 'impact',30
clr = 'black'

speak = w.Dispatch('SAPI.SpVoice')
#*************************************************************download-all********************************************************************
def down():
    speak.Speak("here you can download your youtube videos and songs")
    btn.grid_forget()
    btn2.grid_forget()
    btn3.grid_forget()
    frm.geometry('800x395+300+200')
    frm.resizable(False,False)
    frm.config(background = bgd)
    frm.title("Download-All")
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
            messagebox.showerror('Error','Please enter a youtube link')
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
#***********************************************************************************************************************************************    





#-------------------------------------------------------PASSWORD/GEN----------------------------------------------------------------------------

def psw():
     
    btn3.grid_forget()
    def gen():
        abc = ['a','b','c','d','e','f','j','h','i','g','k','l','m','n','o','p','k','r','s','t','w','x','y','z']
        ABC = ['A','B','C','D','E','F','J','H','I','G','K','L','M','N','O','P','Q','R','S','T','W','X','Y','Z']
        num = ['1','2','3','4','5','6','7','8','9']
        ch = ['@','!','§','?']
        password = ''
        lengh = comb.get()
        lengh = int(lengh)
        if rtrn.get() == 0  :
            
            for i in range(0,lengh//2):
                password+=abc[random.randint(0,23)]
                password+=ABC[random.randint(0,23)]
            pssw = StringVar()
            
            w = Entry(frm,bd=0,textvariable=pssw,state='readonly',readonlybackground=bgd,font=('solid',20),width=40,fg='#60efff')#42
            pssw.set(password)
            
            
            w.grid(row=5,column=0,pady=(25,0))
        
        elif rtrn.get() == 1:
            for i in range(lengh):
                if len(password) < lengh:
                    password+=abc[random.randint(0,23)]
                if len(password) < lengh:
                    password+=ABC[random.randint(0,23)]
                if len(password) < lengh:
                    password+= num[random.randint(0,8)]
                if len(password) < lengh:
                    password+= ch[random.randint(0,3)]
            pssw = StringVar()
            w = Entry(frm,bd=0,textvariable=pssw,state='readonly',readonlybackground=bgd,font=('solid',20),width=40,fg='#60efff')#42
            pssw.set(password)
            
            
            w.grid(row=5,column=0,pady=(25,0))
    speak = w.Dispatch('SAPI.SpVoice')
    speak.Speak('password generator')        
    fnt = ('impact',40)
    btn.grid_forget()
    btn2.grid_forget()
    frm.geometry('800x395+300+200')
    frm.resizable(False,False)
    frm.config(background = bgd)
    frm.title("Password-Gen")
    lbl = Label(frm,text ="Generate Your Code",font=fnt,bg="#60efff",width=30).grid(row=0,column=0,padx=(7,0),pady=(5,30))
    buttonfram = Frame(frm,bg=bgd)
    buttonfram.grid(row=2,column=0)
    combostyle = ttk.Style()

    combostyle.theme_create('combostyle', parent='alt',
                             settings = {'TCombobox':
                                         {'configure':
                                          {'selectbackground': 'black',
                                           'fieldbackground': '#60efff',
                                           'background': 'white'
                                           }}}
                             )
    # ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
    combostyle.theme_use('combostyle') 
    

    
    rtrn = IntVar()
    lista = []
    for i in range(10,100+1):
        lista.append(i)
    weak = Radiobutton(buttonfram,text="weak",bg='#60efff',font=('impact',20),width=10,activebackground='#60efff',value=0,variable=rtrn).grid(row=2,column=0,padx=(0,3))
    strong = Radiobutton(buttonfram,text="strong",bg='#60efff',font=('impact',20),width=10,activebackground='#60efff',value=1,variable=rtrn).grid(row=2,column=1)
    comb = ttk.Combobox(frm,width=10,font=('impact',10),values=lista,state='readonly')
    comb.current(0)
    comb.grid(row=3,column=0,pady=(10,0))
    btn1 = Button(frm,text='Generate',bg="#60efff",width=10,font=("impact",30),command=gen).grid(row=4,column=0,pady=(15,0))
    
    
#-----------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------//time//-------------------------------------------------------------------
def timeme():
    speak.Speak('time now')
    btn.grid_forget()
    btn2.grid_forget()
    btn3.grid_forget()
    frm.title('TIME')
    if dt.time() > datetime.time(12):
        txt = 'PM'
    else:
        txt = 'AM'    
    def display_time():
        crnt_time = tm.strftime(' %H      :    %M     :      %S   ')
        lbl['text'] = crnt_time
        lbl.after(1000,display_time)
    f = Frame(frm,bg=bgd,width=50)
    f.grid(row=3,column=0,padx=1,pady=(10,0))
    
    lbl = Label(frm,font=('impact',60),width=16,bg='#60efff',fg='black')
    lbl1 = Label(frm,font=('impact',60),bg='red',fg='black',text=txt)
    lblh = Label(f,font=('impact',30),bg='red',fg='black',text='Hour')
    lblm = Label(f,font=('impact',30),bg='red',fg='black',text='Minute')
    lbls = Label(f,font=('impact',30),bg='red',fg='black',text='Second')
    

    lbl.grid(row=0,column=0,padx=(20,20),pady=(120,0))
    lbl1.grid(row=0,column=1,padx=(0,130),pady=(120,0))
    lblh.grid(row=1,column=0,padx=(0,130))
    lblm.grid(row=1,column=1,padx=(0,130))
    lbls.grid(row=1,column=2)
    #
    

    
    display_time()
#------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------Info about us ----------------------------------------------------------
def infous():
	btn.grid_forget()
	btn2.grid_forget()
	btn3.grid_forget()
	btn4.grid_forget()
	mg = ImageTk.PhotoImage(file='logo.png')
	l1= Label(frm,image=mg,width=10,height=10).grid(row=0,column=0)

#------------------------------------------------------------------------------------------------------------------------------
frm = Tk()
frm.geometry('800x395+300+200')
frm.resizable(False,False)
frm.config(background = bgd)
frm.title('')
photo = PhotoImage(file = "logo.png")
frm.iconphoto(False, photo)
btn = Button(frm,borderwidth=0,text = 'download',font=('impact',30),bg='#60efff',fg='black',command=down,width=10,cursor='heart')
btn2 = Button(frm,borderwidth=0,text ='Password G',font=(('impact',30)),bg='#60efff',fg='black',command=psw ,cursor='heart')
btn3 = Button(frm,borderwidth=0,font=('impact',30),bg='#60efff',fg='black',command=timeme,text='time',width=10,cursor='heart')
btn4 = Button(frm,borderwidth=0,font=('impact',30),bg='#60efff',fg='black',command=infous,text='about us',width=10,cursor='heart')
btn.grid(row=0,column=0,pady=(100,0),padx=(190,0))
btn2.grid(row=0,column=1,padx=10,pady=(100,0))
btn3.grid(row = 1,column=0,padx=(190,0),pady=(20,0))
#btn4.grid(row=1,column=1,padx=10,pady=(20,0))

frm.mainloop()
