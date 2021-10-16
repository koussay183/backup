#### imports
import tkinter
from tkinter import font
import pygame
from tkinter import*
from tkinter import ttk
import time
from PIL import ImageTk,Image
from sql import *
from tkinter import messagebox
from validate_email import validate_email
from random import randint
import win32com.client as w
import random
from countryinfo import CountryInfo
import pycountry
from lists import cntr_list as cntr_li
from plyer import notification
from gifplayer import *
from sys import platform
from tkinter import filedialog
from download import *
import os 
####
# like fb color = #1e265c
# purple color #1a0067
app_color = '#0c1c34'
# buttons color #5400ec
fnt = 'impact',30
frm = Tk()

combostyle = ttk.Style()
combostyle.theme_create('combostyle', parent='alt',
                        settings = {'TCombobox':
                                    {'configure':
                                        {'selectbackground': 'white',
                                        'selectforeground':'black',
                                        'fieldbackground': 'white',
                                        'background': 'white',
                                        'foreground':'black',
                                        'relief':'flat',
                                        'Combobox.border':'flat'
                                        }}}
                        )

# ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
combostyle.theme_use('combostyle')
#### notification =====
def notif(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = 'apppng\\ttt.ico',
        timeout = 20,
    )
user = open('Data\\log.txt','r')
usern = user.readlines()
usern = usern[0]
usern = usern.replace('\n','')

################################################################### the App #################################################################################
def app():
    
    #notif("Hello "+usern,"Welcome Back")
    def goall():
        l1.place(x=0,y=0,relheight=1,relwidth=1)
        f2.place(x=0,y=658)
        f3.place(x=0,y=0)
    def forgetf4():
        for widget in f4.winfo_children():
                widget.place_forget()
        f4.place_forget()
        f4.place(x=0,y=55)
    def forget(frame):
    	for widget in frame.winfo_children():
    		widget.place_forget()
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def logout():
        f4.place_forget()
        home_btn.place_forget()
        myacc_btn.place_forget()
        logout_btn.place_forget()
        contact_btn.place_forget()
        f2['bg'] = app_color
        f3['bg'] = app_color
        f2['height']='42'
        mainpage()
        d = open('Data\\logs.txt','w')
        d.write('LOGEDOUT')
        d.close()
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   
    def home():
        def returnitall():
            ######"here"#######
            ytb_dl.config(image=dl_btn1)
            play_music.config(image=msc_btn1)
            hover(ytb_dl,dl_btn2,dl_btn1,True)
            hover(play_music,msc_btn2,msc_btn1,True)
            frm.update()
        def hover(widget,new,old,x):
                def clicked(e):
                    returnitall()
                    def ee(e):
                	    pass
                    widget.bind('<Leave>',ee)
                    widget['image']=new
                def init(e):
                    widget['image'] = new
                def out(e):
                    widget['image'] = old
                widget.bind('<Enter>',init)
                widget.bind('<Leave>',out)
                if x == True:
                    widget.bind('<Button-1>',clicked)
                else:
                    pass
        play_msc_frm = Frame(f4,bg=app_color,width=f4['width']-202,height=f4['height'])
        # music player ///////////
        def play_music():
                forget(play_msc_frm)
                pygame.mixer.init()
                play_frm = Frame(play_msc_frm,bg='#1e265c',width=f4['width']-202,height=80)
                list_frm = Frame(play_msc_frm,bg='#1e265c',width=play_msc_frm['width'],height=f4['height']-90)
        	#music 3 playing buttons == 
                play_btn = 'f'
                next_btn = 'f'
                old_btn = 'f'
                #places ====
                play_msc_frm.place(x=202,y=0)
                play_frm.place(x=0,y=510)
                list_frm.place(x=0,y=0)
        # youtube downloder /////
        def download():
            # back end ======
            def download_go():
                try:
                    global path
                    if len(link_entry.get())!=0 and (vd_var.get()== 1 or ad_var.get()==1) and len(path)>1 :
                        if vd_var.get() == 1 :
                            vediodown(link_entry.get(),link_entry,path)
                        else :
                            songdown(link_entry.get(),path)
                    elif len(link_entry.get()) == 0:
                            messagebox.showerror(title=None,message='No Link !')
                    elif vd_var.get() == 0:
                        if ad_var.get()== 1:
                            pass
                        else :
                            messagebox.showerror(title=None,message='No Option !')
                    elif len(path) == 0:
                        messagebox.showerror(title=None,message='NO Path !')
                    else :
                        print('else broo ')
                except NameError :
                        messagebox.showerror(title=None,message="No Path To Save in !")
						                    
            forget(play_msc_frm)
            download_frm = Frame(play_msc_frm,height=play_msc_frm['height'],width=play_msc_frm['width'],bg='#1e265c')
            title_frm = Frame(download_frm,width=download_frm['width'],height=100,bg=download_frm['bg']) 
            title1 = Label(title_frm,text='YouTube',font=("Comic Sans MS",60, "bold"),bg=title_frm['bg'],bd=0,fg='#ff4343')
            title2 = Label(title_frm,text='Downloader',font=("Comic Sans MS", 38, "bold"),bg=title_frm['bg'],bd=0,fg='white')

            opts_frm = Frame(download_frm,height=download_frm['height'],width=360,bg='#5e6ebe')

            
            entry_var = StringVar()
            link_line_lbl = Label(download_frm,font=("Comic Sans MS",20, "bold"),height=2,text='___________________________________',bg=download_frm['bg'],fg='white')
            link_entry = Entry(download_frm,textvariable=entry_var,bd=0,width=37,bg=download_frm['bg'],font=("Comic Sans MS",20, "bold"),fg='white')
            link_lbl = Label(download_frm,text='Link :',anchor=W,width=34,fg='white',font=("Comic Sans MS",25, "bold"),bg=download_frm['bg'],bd=0)
            ytb_logo = Label(opts_frm,image=ytb_logo_img,bg=opts_frm['bg'],bd=0)# show it when download start ==
            download_btn = Button(opts_frm,image=download1,bg=opts_frm['bg'],bd=0,activebackground=opts_frm['bg'],command=download_go)

            hover(download_btn,download2,download1,False)
            vd_var = IntVar()
            ad_var = IntVar()
            vedio = Checkbutton(opts_frm,text='Vedio',variable=vd_var,font=("Comic Sans MS",17, "bold"),fg=app_color,bg=opts_frm['bg'],activebackground=opts_frm['bg'],activeforeground=app_color)
            audio = Checkbutton(opts_frm,text='Music',variable=ad_var,font=("Comic Sans MS",17, "bold"),fg=app_color,bg=opts_frm['bg'],activebackground=opts_frm['bg'],activeforeground=app_color)

            desc = Label(download_frm,text='Welcome , Here You Can Download Your YouTube'+"\n"+'Vedios And Songs Just, Take The Link From'+"\n"+'YouTube And Paste It In The link Entry Then'+"\n"+'Choise Options To Download....',fg="white",bg=download_frm['bg'],font=("Comic Sans MS",20, "bold"),width=38,height=4,anchor=NW,justify=LEFT)
            # ask for file to save in //////
            path = ''
            def browse_button():
                global path 
                filename = filedialog.askdirectory()
                path = os.path.abspath(str(filename))
                path = path.replace('\\','\\\\')
                print(path)
            save_in_btn = Button(download_frm,image=browse1,activebackground=download_frm['bg'],bg=download_frm['bg'],command=browse_button,bd=0)
            hover(save_in_btn,browse2,browse1,False)
            svin_lbl = Label(download_frm,text='Save In :',font=("Comic Sans MS",17, "bold"),bg=download_frm['bg'],fg='white')
            
            
            # place ====
            download_frm.place(x=0,y=0)

            title_frm.place(x=0,y=0)
            title1.place(x=60,y=0)
            title2.place(x=385,y=30)

            opts_frm.place(x=750,y=0)

            ytb_logo.place(x=70,y=100)

            link_lbl.place(x=60,y=360)
            link_entry.place(x=60,y=400)
            link_line_lbl.place(x=60,y=390)

            download_btn.place(x=50,y=500)
            vedio.place(x=180,y=450)
            audio.place(x=70,y=450)

            desc.place(x=40,y=155)

            save_in_btn.place(x=190,y=470)
            svin_lbl.place(x=60,y=474)
            
        forgetf4()

        apps_frame = Frame(f4,bg='white',height=590,width=202)
        ytb_dl = Button(apps_frame,image=dl_btn1,bg=apps_frame['bg'],bd=0,command=download)
        play_music = Button(apps_frame,image=msc_btn2,bg=apps_frame['bg'],bd=0,command=play_music)

        
        hover(ytb_dl,dl_btn2,dl_btn1,True)
        hover(play_music,msc_btn2,msc_btn1,True)
        #play_music.bind('<Leave>',lambda e : True )
        ytb_dl.invoke()
    	#forget=====
        f2.place_forget()
        ## places ======
        f2.place(x=0,y=658)
        apps_frame.place(x=0,y=0)
        apps_frame.grid_propagate(0)
        ytb_dl.grid(row=1,column=0)
        # play_music.grid(row=0,column=0)
        
        
    # here open the images :
        
    dl_btn1 = ImageTk.PhotoImage(file='apppng\\home\\ydl1.png')
    dl_btn2 = ImageTk.PhotoImage(file='apppng\\home\\ydl2.png')

    msc_btn1 = ImageTk.PhotoImage(file="apppng\\home\\music1.png")
    msc_btn2 = ImageTk.PhotoImage(file="apppng\\home\\music2.png")
    # opning ytb logo and resize it 
    ytb_img_n = Image.open('apppng\\home\\downloader\\ytb_logo.png')
    ytb_img_r = ytb_img_n.resize((200,190),Image.ANTIALIAS)
    ytb_logo_img = ImageTk.PhotoImage(ytb_img_r,master=frm)
    # download button image here ===
    download1 = ImageTk.PhotoImage(file='apppng\\home\\downloader\\down_btn1.png')
    download2 = ImageTk.PhotoImage(file='apppng\\home\\downloader\\down_btn2.png')
    # browse button  ===
    browse1 = ImageTk.PhotoImage(file='apppng\\home\\downloader\\browse1.png')
    browse2 = ImageTk.PhotoImage(file='apppng\\home\\downloader\\browse2.png')
    # playing music buttons ==
    play_btn_img = 'f'
    next_btnimg ='f'
    old_btn_img ='f'  
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++myacc all settings ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++myacc all settings ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
    def myacc():
        bgall='#1e265c'
        forgetf4()
        forget(info_frm)
        all()
        bnd1()
        bnd2()
        bnd3()
        bnd4()
        bnd5()
        
        fgall="white"
        info_frm['bg']=bgall
        
        lblx1 = Label(info_frm,height=info_frm['height'],width=2,bg=fgall)
        last_info_f = Frame(info_frm,height=490,width=490,bg=bgall,highlightbackground=bgall,highlightthickness=4)
        userget = open('Data\\log.txt')
        usern = userget.readline()
        Font_tuple = ("Comic Sans MS", 24, "bold") 
        wlcm_lbl = Label(info_frm,fg=fgall,anchor=W,width=16,justify=LEFT,text='Hello '+usern+"We are Trying"+"\n"+"The Best ,"+"\n"+"To Give You"+"\n"+"a Patients Service"+"\n"+"You Can Contact Us"+"\n"+"Whenever You Want"+"\n"+"And Ask Any"+"\n"+"Question You Want"+"\n"+"We Are Waiting"+"\n"+"For You",bg=bgall)
        wlcm_lbl.configure(font = Font_tuple)
        space_lbl = Label(info_frm,image=space,bg=bgall,bd=0)
        info_frm['height']=f4['height']
        info_frm['width']=f4['width']
        # places ======
        frm_lbl.place(x=0,y=0)
        info_frm.place(x=360,y=0)#y as 35
        xb = 18
        mydt_btn.place(x=xb,y=200)
        changemail_btn.place(x=xb,y=275)
        changeuser_btn.place(x=xb,y=350)
        changepss_btn.place(x=xb,y=425)
        changeph_btn.place(x=xb,y=500)

        sml_lbl.place(x=36,y=20)
        space_lbl.place(x=360,y=0)
        wlcm_lbl.place(x=40,y=40)

        lblx1.place(x=0,y=0)
        #last_info_f.place(x=10,y=13)
    
    f4 = Frame(frm,width=1300,height=590,bg='#0c1c34')
    f2['bg'] = '#0c1c34'
    f3['bg'] = '#0c1c34'
    f2['height'] = '44'
    # images open here and resize here ====
 
    #frm_lbl = Label(f4,image=frm_img,bd=0,bg='#0c1c34')
    frm_lbl = Frame(f4,height=f4['height'],width=360,bg='#5e6ebe')

    # small logo in frame of options =====
    sml_not = Image.open('apppng\\1.png')
    sml = sml_not.resize((230,145),Image.ANTIALIAS)
    sml = ImageTk.PhotoImage(sml,master=frm)
    sml_lbl = Label(f4,image=sml,bd=0,bg=frm_lbl['bg'])
    #space frame ===============
    space_not = Image.open('apppng\\myacc\\space.png')
    space = space_not.resize((620,570),Image.ANTIALIAS)
    space = ImageTk.PhotoImage(space,master=frm)
    # btns options ==========================================================
    # buttons chnage defs ----------------
    def enter1(event):
    	mydt_btn['image']=mydt_img2
    def leave1(event):
    	mydt_btn['image'] =mydt_img1

    def enter2(event):
    	changepss_btn['image']=change_pss2
    def leave2(event):
    	changepss_btn['image'] =change_pss1 

    def enter3(event):
    	changeuser_btn['image']=change_user2
    def leave3(event):
    	changeuser_btn['image'] =change_user1 

    def enter4(event):
    	changeph_btn['image']=change_ph2
    def leave4(event):
    	changeph_btn['image'] =change_ph1

    def enter5(event):
    	changemail_btn['image']=change_mail2
    def leave5(event):
    	changemail_btn['image'] =change_mail1 
    
    def all():
    	mydt_btn['image'] =mydt_img1
    	changepss_btn['image'] =change_pss1
    	changeuser_btn['image'] =change_user1
    	changeph_btn['image'] =change_ph1
    	changemail_btn['image'] =change_mail1
    
    def bnd1():
    	mydt_btn.bind('<Enter>',enter1)
    	mydt_btn.bind('<Leave>',leave1)
    def bnd2():
    	changepss_btn.bind('<Enter>',enter2)
    	changepss_btn.bind('<Leave>',leave2)
    def bnd3():
    	changeuser_btn.bind('<Enter>',enter3)
    	changeuser_btn.bind('<Leave>',leave3)
    def bnd4():
    	changeph_btn.bind('<Enter>',enter4)
    	changeph_btn.bind('<Leave>',leave4)
    def bnd5():
    	changemail_btn.bind('<Enter>',enter5)
    	changemail_btn.bind('<Leave>',leave5)
    def returnit(name):
    	if name == 'mydt_btn':
    		bnd2()
    		bnd3()
    		bnd4()
    		bnd5()
    	elif name == 'changepss_btn':
    		bnd1()
    		bnd3()
    		bnd4()
    		bnd5()
    	elif name == 'changeuser_btn':
    		bnd1()
    		bnd2()
    		bnd4()
    		bnd5()
    	elif name == 'changeph_btn':
    		bnd1()
    		bnd2()
    		bnd3()
    		bnd5()
    	elif name == 'changemail_btn':
    		bnd1()
    		bnd2()
    		bnd3()
    		bnd4()   	       			
    def go(event):
        pass
    ###### my dtails button configs ==============
    def wc1(event):
        info_frm.place(x=360,y=0)#y as 35
        info_frm['bg']='#1e265c'
        info_frm['height']=f4['height']
        info_frm['width']=f4['width']
        returnit('mydt_btn')
        mydt_btn.bind('<Enter>',go)
        mydt_btn.bind('<Leave>',go)
        all()
        bgall='#1e265c'
        fgall='white'
        fontall = "Comic Sans MS"
        info_last_one = ImageTk.PhotoImage(file='apppng\\last_info_frm.png')
        mydt_btn['image'] = mydt_img2
        forget(info_frm)
        info_img_lbl = Label(info_frm,image=info_img,bg='#cccccc',bd=0)#,height=300,width=300
        last_info_ff = Frame(info_frm,height=info_frm['height'],width=505,bg='#1e265c')#'#f5f5f5'
        
        lblx1 = Label(info_frm,text='Personal Informations',font=(fontall, 30, "bold"),bg=bgall,fg=fgall)
        lblx2 = Label(info_frm,image=info_last_one,bg=bgall)
        user = open('Data\\log.txt','r')
        usern = user.readlines()
        usern = usern[0]
        usern = usern.replace('\n','')
        dbrun("USE easylife") 
        SQL_get = dbget("SELECT username ,email,phone,password FROM users WHERE username = '%s'"%(usern))
        username = SQL_get[0][0]
        email = SQL_get[0][1]
        phone = SQL_get[0][2]
        password = SQL_get[0][3]
        lblusername = Label(info_frm,text='Username : '+str(username),font=(fontall, 24, "bold"),bg=bgall,fg=fgall)
        lblemail = Label(info_frm,text='E-Mail : '+str(email),font=(fontall, 24, "bold"),bg=bgall,fg=fgall)
        lblphone = Label(info_frm,text='Phone - Number : '+str(phone),font=(fontall, 24, "bold"),bg=bgall,fg=fgall)
        star = len(password)*'*'
        lblpassword = Label(info_frm,text='Password : '+str(star),font=(fontall, 24, "bold"),bg=bgall,fg=fgall)
        sc_lbl = Label(info_frm,text='Your Data Is Safe With Us',font=(fontall, 22, "bold"),bg=bgall,fg=fgall)
        lblx3 = Label(info_frm,height=21,width=2,bg=fgall)
        lblx4 = Label(info_frm,height=4,width=2,bg=fgall)
        lblx5 = Label(info_frm,height=3,width=2,bg=fgall)

        lblx6 = Label(info_frm,height=info_frm['height'],width=31,bg=fgall)
        lblx7 = Label(info_frm,text='E\nA\nS\nY',font=(fontall,70, "bold"),fg='#5e6ebe',bg=lblx6['bg'])
        lblx8 = Label(info_frm,text='L\nI\nF\nE',font=(fontall,70, "bold"),fg='#5e6ebe',bg=lblx6['bg'])
    	#places===========
        xinfo = 50

        #info_img_lbl.place(x=500,y=0)
        last_info_ff.place(x=0,y=0)
        lblx1.place(x=xinfo,y=15)
        #lblx2.place(x=32,y=80)

        
        lblusername.place(x=xinfo,y=135)
        lblemail.place(x=xinfo,y=225)
        lblphone.place(x=xinfo,y=315)
        lblpassword.place(x=xinfo,y=405)

        lblx3.place(x=10,y=140)
        lblx4.place(x=10,y=13)
        lblx5.place(x=10,y=525)

        lblx6.place(x=720,y=0)
        lblx7.place(x=737,y=20)
        lblx8.place(x=850,y=20)

        sc_lbl.place(x=xinfo,y=525)

        frm.mainloop()
    ## chnage password btn config ========================================	
    def wc2(event):
        info_frm.place(x=385,y=35)#y as 35
        backfrm()
        bgall = "#1e265c"
        fgall = 'white'
        def saveit():
            user = open('Data\\log.txt','r')
            usern = user.readlines()
            usern = usern[0]
            usern = usern.replace('\n','')
            dbrun("USE easylife") 
            SQL_get = dbget("SELECT password FROM users WHERE username = '%s'"%(usern))
            password = SQL_get[0][0]
            if 8<=len(new_password_var.get())<=16 and  password_var.get() == password:
            	bgallag()
            	dbrun("UPDATE users SET password = '%s' WHERE username = '%s'"%(new_password_var.get(),usern))
            	messagebox.showinfo(title=None,message='Changes Successfully Saved')
            	f = open('password.txt','w')
            	f.write(new_password_var.get())
            	f.close()
            	password_var.set('')
            	new_password_var.set('')

            elif 8>len(new_password_var.get())>16 :
            	bgallag()
            	line2['fg']='red'
            	messagebox.showerror(title=None,message='Please Enter Password Consists At Less From 8 letters And Don\'t Pass 16 Letters')
            	new_password_var.set('')
            elif password_var.get() != password : 
            	bgallag()
            	line1['fg']='red'
            	messagebox.showerror(title=None,message='Wrong password')
            else :
            	bgallag()
            	line2['fg']='red'
            	messagebox.showerror(title=None,message='Please Use Some Numbers in Your New Password')
        info_frm['bg']=fgall
        returnit('changepss_btn')
        changepss_btn.bind('<Enter>',go)
        changepss_btn.bind('<Leave>',go)
        all()
        changepss_btn['image'] =change_pss2
        forget(info_frm)
        
        def bgallag():
                line1['fg']=fgall
                line2['fg']=fgall
        def backitall(event):
            line1['text']='___________________'
            line2['text']='___________________'
            frm.update()

        info_frm['bg']=fgall
        def widthit(widget,line):
            def do(event):
                line1['text']='___________________'
                line2['text']='___________________'
                line['text'] ='____________________'    
            widget.bind('<Button-1>',do)
            frm.update()

        sc_on_lbl = Label(info_frm,image=sc_on_img,bg=fgall,bd=0)
        
        fontt = ("Comic Sans MS", 20, "bold")
        fonttt = ("Comic Sans MS", 24, "bold")
        
        holder = Frame(info_frm,bg=bgall,height=info_frm['height'],width=428)
        
        line1 = Label(info_frm,text='___________________',font=fonttt,fg=fgall,bd=0,bg=bgall)
        line2 = Label(info_frm,text='___________________',font=fonttt,fg=fgall,bd=0,bg=bgall)
        

        password_var = StringVar()
        new_password_var = StringVar()

        password_entry = Entry(info_frm,show='*',textvariable=password_var,fg=fgall,width=43,bg=bgall,bd=0,font=('tahoma',13))
        new_password = Entry(info_frm,textvariable=new_password_var,fg=fgall,width=43,bg=bgall,bd=0,font=('tahoma',13))
        
        widthit(password_entry,line1)
        widthit(new_password,line2)

        lblx1 = Label(info_frm,text='Current Password',font=fontt,bg=bgall,fg=fgall)
        lblx2 = Label(info_frm,text='New password',font= fontt,bg=bgall,fg=fgall)
        
        
        info_frm.bind("<Button-1>",backitall)
        # when you click on the frame foucs romove frim entrys and entrys return to the old positions
        info_frm.bind_all("<1>", lambda event:event.widget.focus_set())
        sc_on_lbl.bind_all("<1>", lambda event:event.widget.focus_set())
        sc_on_lbl.bind('<1>',backitall)
        holder.bind('<1>',backitall)
        save_btn = Button(info_frm,command=saveit,bd=0,image=save_img2,bg=bgall,activebackground=bgall)
        def f(event):
            save_btn['image']=save_img2
        def y(event):
            save_btn['image']=save_img1
        save_btn.bind('<Enter>',y)
        save_btn.bind('<Leave>',f)
        
        #places
        sc_on_lbl.place(x=380,y=50)
        holder.place(x=0,y=0)
        
        lblx2.place(x=15,y=137)
        new_password.place(x=15,y=180)
        line2.place(x=15,y=165)


        lblx1.place(x=15,y=237)
        password_entry.place(x=15,y=280)
        line1.place(x=15,y=265)

        save_btn.place(x=115,y=400)
    
    ## change username btn config =========================================
    def wc3(event):
        info_frm.place(x=385,y=35)#y as 35
        backfrm()
        bgall = "#1e265c"
        fgall='white'
        def bgallag():
                line1['fg']=fgall
                line2['fg']=fgall
        # back end to change username and chaking if username can be used=============================

        def saveit():
            from cheker import checkusername
            user = open('Data\\log.txt','r',encoding='cp1252')
            usern = user.readlines()
            usern = usern[0]
            usern = usern.replace('\n','')
            dbrun("USE easylife") 
            SQL_get = dbget("SELECT password FROM users WHERE username = '%s'"%(usern))
            password = SQL_get[0][0]
            is_valid_username = checkusername(username_var.get(),username_var)
            old = usern
            if len(username_var.get()) >= 4 and len(username_var.get()) <= 10 and  password == password_var.get() and is_valid_username == 1 :
                bgallag()
                dbrun("UPDATE users SET username = '%s' WHERE username = '%s'"%(username_var.get(),usern))
                messagebox.showinfo(title=None,message='Changes Successfully Saved')
                f = open('Data\\log.txt','r')
                ff=f.read()
                ff = str(ff)
                ff = ff.replace(str(usern),username_var.get())
                f.close()
                x = open('Data\\log.txt','w')
                x.write(ff)
                x.close()
                username_var.set('')
                password_var.set('')
            elif len(username_var.get()) == 0 or len(password_var.get())==0:
                bgallag()
                line1['fg'] = 'red'
                line2['fg'] = 'red'
                messagebox.showerror(title=None,message='Give All The Informations')
            elif  len(str(username_var.get())) < 4 or len(str(username_var.get())) > 10:
                bgallag()
                line2['fg'] = 'red'
                username_var.set('')
                messagebox.showerror(title=None,message="Please Enter Username Consists At Less From 4 letters And Don't Pass 10 Letters")
            elif password != password_var.get():
                bgallag()
                line1['fg']='red'
                messagebox.showerror(title=None,message='Wrong Passwrod')
            else :
                print('else')
        #==============================================================================================
        
        def backitall(event):
            line1['text']='___________________'
            line2['text']='___________________'
            frm.update()
        info_frm['bg']=fgall
        returnit('changeuser_btn')
        changeuser_btn.bind('<Enter>',go)
        changeuser_btn.bind('<Leave>',go)
        all()
        changeuser_btn['image'] =change_user2
        forget(info_frm)

        
        def widthit(widget,line):
            def do(event):
                line1['text']='___________________'
                line2['text']='___________________'
                line['text'] ='____________________'    
            widget.bind('<Button-1>',do)
            frm.update()

        username_ppl_lbl = Label(info_frm,image=username_ppl,bg=fgall,bd=0)
        fontt = ("Comic Sans MS", 20, "bold")
        fonttt = ("Comic Sans MS", 24, "bold")
        
        holder = Frame(info_frm,bg=bgall,height=info_frm['height'],width=428)
        
        line1 = Label(info_frm,text='___________________',font=fonttt,fg=fgall,bd=0,bg=bgall)
        line2 = Label(info_frm,text='___________________',font=fonttt,fg=fgall,bd=0,bg=bgall)
        

        password_var = StringVar()
        username_var = StringVar()

        password_entry = Entry(info_frm,show='*',textvariable=password_var,fg=fgall,width=43,bg=bgall,bd=0,font=('tahoma',13))
        new_usernamee = Entry(info_frm,textvariable=username_var,fg=fgall,width=43,bg=bgall,bd=0,font=('tahoma',13))
        
        widthit(password_entry,line1)
        widthit(new_usernamee,line2)

        lblx1 = Label(info_frm,text='Current Password',font=fontt,bg=bgall,fg=fgall)
        lblx2 = Label(info_frm,text='New Username',font= fontt,bg=bgall,fg=fgall)
        
        
        info_frm.bind("<Button-1>",backitall)
        # when you click on the frame foucs romove frim entrys and entrys return to the old positions
        info_frm.bind_all("<1>", lambda event:event.widget.focus_set())
        username_ppl_lbl.bind_all("<1>", lambda event:event.widget.focus_set())
        username_ppl_lbl.bind('<1>',backitall)
        holder.bind('<1>',backitall)
        save_btn = Button(info_frm,command=saveit,bd=0,image=save_img2,bg=bgall,activebackground=bgall)
        def f(event):
            save_btn['image']=save_img2
        def y(event):
            save_btn['image']=save_img1
        save_btn.bind('<Enter>',y)
        save_btn.bind('<Leave>',f)
        
        #places
        username_ppl_lbl.place(x=427,y=100)
        holder.place(x=0,y=0)
        
        lblx2.place(x=15,y=137)
        new_usernamee.place(x=15,y=180)
        line2.place(x=15,y=165)


        lblx1.place(x=15,y=237)
        password_entry.place(x=15,y=280)
        line1.place(x=15,y=265)

        save_btn.place(x=115,y=400)

    # change phone number config ========================================== 
    def wc4(event):
        info_frm.place(x=385,y=35)#y as 35
        backfrm()
        bgall = "#1e265c"
        fgall = 'white'
        def saveitee():
            user = open('Data\\log.txt','r',encoding='cp1252')
            usern = user.readlines()
            usern = usern[0]
            usern = usern.replace('\n','')
            dbrun("USE easylife") 
            SQL_get = dbget("SELECT password FROM users WHERE username = '%s'"%(usern))
            password = SQL_get[0][0]

            if len(str(new_phone.get())) <= 12 and len(str(new_phone.get())) >= 8 and password_entry.get() == password:
                bgallag()
                messagebox.showinfo(title=None,message='Changes Successfully Saved')
                dbrun("UPDATE users SET phone = '%s' WHERE username = '%s'"%(str(new_phone.get()),str(usern)))
                new_phone_var.set('')
                password_var.set('')
            elif len(str(new_phone.get()))>12 or len(str(new_phone.get()))< 8 :
                bgallag()
                line2['fg']='red'
                new_phone_var.set('')
                messagebox.showerror(title=None,message='Please Enter a Valid Number')
            elif password_entry.get() == password :
                password_var.set('')
                line1['fg']='red'
                messagebox.showerror(title=None,message='Wrong Password')
            else :
                print('!!!!')
        info_frm['bg']=fgall
        returnit('changeph_btn')
        changeph_btn.bind('<Enter>',go)
        changeph_btn.bind('<Leave>',go)
        all()
        changeph_btn['image'] =change_ph2
        forget(info_frm)
        
        
        def bgallag():
                line1['fg']=fgall
                line2['fg']=fgall
        def backitall(event):
            line1['text']='___________________'
            line2['text']='___________________'
            frm.update()

        info_frm['bg']=fgall
        def widthit(widget,line):
            def do(event):
                line1['text']='___________________'
                line2['text']='___________________'
                line['text'] ='____________________'    
            widget.bind('<Button-1>',do)
            frm.update()

        call_lbl = Label(info_frm,image=call_img,bg=fgall,bd=0)
        
        fontt = ("Comic Sans MS", 20, "bold")
        fonttt = ("Comic Sans MS", 24, "bold")
        
        holder = Frame(info_frm,bg=bgall,height=info_frm['height'],width=428)
        
        line1 = Label(info_frm,text='___________________',font=fonttt,fg=fgall,bd=0,bg=bgall)
        line2 = Label(info_frm,text='___________________',font=fonttt,fg=fgall,bd=0,bg=bgall)
        

        password_var = StringVar()
        new_phone_var = StringVar()

        password_entry = Entry(info_frm,show='*',textvariable=password_var,fg=fgall,width=43,bg=bgall,bd=0,font=('tahoma',13))
        new_phone = Entry(info_frm,textvariable=new_phone_var,fg=fgall,width=43,bg=bgall,bd=0,font=('tahoma',13))
        
        widthit(password_entry,line1)
        widthit(new_phone,line2)

        lblx1 = Label(info_frm,text='Current Password',font=fontt,bg=bgall,fg=fgall)
        lblx2 = Label(info_frm,text='New Phone-Number',font= fontt,bg=bgall,fg=fgall)

        
        info_frm.bind("<Button-1>",backitall)
        # when you click on the frame foucs romove frim entrys and entrys return to the old positions
        
        info_frm.bind_all("<1>", lambda event:event.widget.focus_set())
        call_lbl.bind_all("<1>", lambda event:event.widget.focus_set())
        call_lbl.bind('<1>',backitall)
        holder.bind('<1>',backitall)
        save_btn = Button(info_frm,command=saveitee,bd=0,image=save_img2,bg=bgall,activebackground=bgall)
        def f(event):
            save_btn['image']=save_img2
        def y(event):
            save_btn['image']=save_img1
        save_btn.bind('<Enter>',y)
        save_btn.bind('<Leave>',f)
        
        #places
        
        call_lbl.place(x=321,y=55)
        holder.place(x=0,y=0)
        
        lblx2.place(x=15,y=137)
        new_phone.place(x=15,y=180)
        line2.place(x=15,y=165)


        lblx1.place(x=15,y=237)
        password_entry.place(x=15,y=280)
        line1.place(x=15,y=265)

        save_btn.place(x=115,y=400)


    ###### change email button configs=============================================
    def wc5(event):
        info_frm.place(x=385,y=35)#y as 35
        backfrm()
        bgall = "#1e265c" #fb6c73
        fgall='white'
        def backitall(event):
            line1['text']='___________________'
            line2['text']='___________________'
            line3['text']='___________________'
            frm.update()
        # back end to chnage email =====================================================================
        def saveit():
            from regexx import checkit

            dbrun("USE easylife") 
            check_if_email_used = dbget("SELECT email FROM users WHERE email = '%s'"%(str(new_email.get())))

            
            is_validd = checkit(str(new_email_var.get()))
            

            user = open('Data\\log.txt','r')
            usern = user.readlines()
            usern = usern[0]
            usern = usern.replace('\n','')
            SQL_get = dbget("SELECT password FROM users WHERE username = '%s'"%(usern))
            passwordd = SQL_get[0][0]

            
            def bgallag():
                line1['fg']=fgall
                line2['fg']=fgall
                line3['fg']=fgall

            if len(check_if_email_used)==0 and is_validd==True and passwordd == password_var.get() and (len(new_email_var.get())!=0 and len(confirm_var.get())!=0 and len(password_var.get())!=0):
                bgallag()
                line1['text']='___________________'
                line2['text']='___________________'
                line3['text']='___________________'

                dbrun("UPDATE users SET email ='%s' WHERE username = '%s'"%(new_email_var.get(),usern))
                messagebox.showinfo(title=None,message='Changes Successfully Saved')
                password_var.set('')
                new_email_var.set('')
                confirm_var.set('')

            elif len(new_email.get())==0 or len(confirm.get())==0 or len(password.get())==0:
                bgallag()
                line1['text']='___________________'
                line2['text']='___________________'
                line3['text']='___________________'
                line1['fg']='red'
                line2['fg']='red'
                line3['fg']='red'
                messagebox.showwarning(title=None,message='Give All The Informations')
            elif len(check_if_email_used)!=0:
                bgallag()
                line2['fg']='red'
                line3['fg']='red'
                messagebox.showerror(title=None,message='This E-Mail Already')
                new_email_var.set('')
                confirm_var.set('')

            elif is_validd==False:
                bgallag()
                line2['fg']='red'
                line3['fg']='red'
                messagebox.showerror(title=None,message='This E-Mail Not Exist')
                new_email_var.set('')
                confirm_var.set('')

            elif passwordd != password.get():
                bgallag()
                line1['fg']='red'
                messagebox.showwarning(title=None,message='Wrong Password')
                password_var.set('')
            else :
                print('else')

        #==========================================================================================================

        info_frm['bg']=fgall

        def widthit(widget,line):
            def do(event):
                line1['text']='___________________'
                line2['text']='___________________'
                line3['text']='___________________'
                line['text'] ='____________________'    
            widget.bind('<Button-1>',do)
            frm.update()
        
        returnit('changemail_btn')	
        changemail_btn.bind('<Enter>',go)
        changemail_btn.bind('<Leave>',go)
        all()
        changemail_btn['image'] =change_mail2
        forget(info_frm)

        email_lbl = Label(info_frm,image=email_img,bg=fgall,bd=0)

        fontt = ("Comic Sans MS", 20, "bold")
        fonttt = ("Comic Sans MS", 24, "bold")
        
        holder = Frame(info_frm,bg=bgall,height=info_frm['height'],width=428)
        
        line1 = Label(info_frm,text='___________________',font=fonttt,fg=fgall,bd=0,bg=bgall)
        line2 = Label(info_frm,text='___________________',font=fonttt,fg=fgall,bd=0,bg=bgall)
        line3 = Label(info_frm,text='___________________',font=fonttt,fg=fgall,bd=0,bg=bgall)

        password_var = StringVar()
        new_email_var = StringVar()
        confirm_var = StringVar()
        password = Entry(info_frm,show='*',textvariable=password_var,fg=fgall,width=43,bg=bgall,bd=0,font=('tahoma',13))
        new_email = Entry(info_frm,textvariable=new_email_var,fg=fgall,width=43,bg=bgall,bd=0,font=('tahoma',13))
        confirm = Entry(info_frm,fg=fgall,textvariable=confirm_var,width=43,bg=bgall,bd=0,font=('tahoma',13))
        widthit(password,line1)
        widthit(confirm,line3)
        widthit(new_email,line2)

        lblx1 = Label(info_frm,text='Current Password',font=fontt,bg=bgall,fg=fgall)
        lblx2 = Label(info_frm,text='New E-Mail',font= fontt,bg=bgall,fg=fgall)
        lblx3 = Label(info_frm,text='Confirm E-Mail',font= fontt,bg=bgall,fg=fgall)
        
        info_frm.bind("<Button-1>",backitall)
        # when you click on the frame foucs romove frim entrys and entrys return to the old positions
        info_frm.bind_all("<1>", lambda event:event.widget.focus_set())
        email_lbl.bind_all("<1>", lambda event:event.widget.focus_set())
        email_lbl.bind('<1>',backitall)
        holder.bind('<1>',backitall)
        save_btn = Button(info_frm,command=saveit,bd=0,image=save_img2,bg=bgall,activebackground=bgall)
        def f(event):
            save_btn['image']=save_img2
        def y(event):
            save_btn['image']=save_img1
        save_btn.bind('<Enter>',y)
        save_btn.bind('<Leave>',f)
        
        #places
        email_lbl.place(x=427,y=50)
        holder.place(x=0,y=0)
        
        lblx2.place(x=15,y=87)
        new_email.place(x=15,y=130)
        line2.place(x=15,y=115)

        lblx3.place(x=15,y=187)
        confirm.place(x=15,y=230)
        line3.place(x=15,y=215)

        lblx1.place(x=15,y=287)
        password.place(x=15,y=330)
        line1.place(x=15,y=315)

        save_btn.place(x=115,y=400)
    #------------------------------------------------------------------------------------------------
    mydt_img1 = ImageTk.PhotoImage(file='apppng\\myacc\\mydt1.png')
    mydt_img2 = ImageTk.PhotoImage(file='apppng\\myacc\\mydt2.png')
    mydt_btn = Button(f4,image=mydt_img1,bd=0,bg=frm_lbl['bg'],activebackground=frm_lbl['bg'])
    bnd1()
    mydt_btn.bind('<Button-1>',wc1)
    #----------
    change_pss1 = ImageTk.PhotoImage(file='apppng\\myacc\\changepss1.png')
    change_pss2 = ImageTk.PhotoImage(file='apppng\\myacc\\changepss2.png')
    changepss_btn = Button(f4,image=change_pss1,bd=0,bg=frm_lbl['bg'],activebackground=frm_lbl['bg'])
    bnd2()
    changepss_btn.bind('<Button-1>',wc2)
    #----------
    change_user1 = ImageTk.PhotoImage(file='apppng\\myacc\\changeuser1.png')
    change_user2 = ImageTk.PhotoImage(file='apppng\\myacc\\changeuser2.png')
    changeuser_btn = Button(f4,image=change_user1,bd=0,bg=frm_lbl['bg'],activebackground=frm_lbl['bg'])
    bnd3()
    changeuser_btn.bind('<Button-1>',wc3)
    #----------
    change_ph1 = ImageTk.PhotoImage(file='apppng\\myacc\\changeph1.png')
    change_ph2 = ImageTk.PhotoImage(file='apppng\\myacc\\changeph2.png')
    changeph_btn = Button(f4,image=change_ph1,bd=0,bg=frm_lbl['bg'],activebackground=frm_lbl['bg'])
    bnd4()
    changeph_btn.bind('<Button-1>',wc4)
    #----------
    change_mail1 = ImageTk.PhotoImage(file='apppng\\myacc\\changemail1.png')
    change_mail2 = ImageTk.PhotoImage(file='apppng\\myacc\\changemail2.png')
    changemail_btn = Button(f4,image=change_mail1,bd=0,bg=frm_lbl['bg'],activebackground=frm_lbl['bg'])
    bnd5()
    changemail_btn.bind('<Button-1>',wc5)
    #------------------------------------------------------------------------------------------------
    infos_not = Image.open('apppng\\myacc\\infos.png')
    info_img1 = infos_not.resize((390,520),Image.ANTIALIAS)
    info_img= ImageTk.PhotoImage(info_img1,master=frm)
    ##=====
    email_img = Image.open('apppng\\myacc\\email.png')
    email_img_r = email_img.resize((500,400),Image.ANTIALIAS)
    email_img=ImageTk.PhotoImage(email_img_r,master=frm)
    ##======
    save_img1 = ImageTk.PhotoImage(file='apppng\\myacc\\save1.png')
    save_img2 = ImageTk.PhotoImage(file='apppng\\myacc\\save2.png')
    ##======
    username_ppl_not = Image.open('apppng\\myacc\\username_ppl.png')
    username_ppl_r = username_ppl_not.resize((460,420),Image.ANTIALIAS)
    username_ppl = ImageTk.PhotoImage(username_ppl_r,master=frm)
    ##======
    sc_on_not = Image.open('apppng\\myacc\\sc_on.png')
    sc_on_y = sc_on_not.resize((550,430),Image.ANTIALIAS)
    sc_on_img = ImageTk.PhotoImage(sc_on_y,master=frm)
    ##======
    call_not = Image.open('apppng\\myacc\\call.png')
    call_y = call_not.resize((630,430),Image.ANTIALIAS)
    call_img = ImageTk.PhotoImage(call_y,master=frm)
    ##======
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def contact():
        
        forgetf4()
        #f1 = Frame(f4,bg='#66fcf1',height=100,width=f4['width'])
        #lbl = Label(f4,image=img1,bd=0)
        msg_frm = Frame(f4,bg=app_color,height=470,width=500)#'#2b7a78'
        lbl1 = Label(msg_frm,text='Write Your Message For Us',bg=app_color,fg='white',font=("Comic Sans MS", 20, "bold"))
        msg = Text(msg_frm,fg='white',tabs=10,width=47,highlightthickness=4,highlightbackground='white' ,relief=FLAT,borderwidth=4,height=10,font=("Comic Sans MS", 13, "bold"),bg='#1e265c')
        msg.insert("end",'type here.....')
        def goahed(e):
            if msg.get(1.0, "end-1c") == 'type here.....' :
        	    msg.delete(1.0, "end-1c")
        msg.bind('<Button-1>',goahed)
        imgs_frm = Frame(f4,bd=0,bg='white',width=665,height=490)
        el_lbl2 = Label(imgs_frm,text='Better Live',font=("Comic Sans MS", 45 , "bold"),bg='white',fg='#5e6ebe')
        el_lbl = Label(imgs_frm,text='Easy Life',font=("Comic Sans MS", 80 , "bold"),anchor=W,justify='left',bg='white',fg='#5e6ebe')
        img_rv = Label(imgs_frm,image=reviw_img,bd=0,bg='#5e6ebe',width=700,height=200)#anchor=CENTER,justify=CENTER
        after_snd = Label(f4,image=after_snd_img,bd=0,bg=app_color)
        lbl5 = Label(f4,bg=app_color,width=45,height=210,bd=0)
        txt_after = Label(f4,text='Successfully Sent',bg=app_color,fg='white',font=("Comic Sans MS", 90 , "bold"))
        f1 = Frame(f4,bg='#1e265c',height=100,width=f4['width'])
        def send_sms():

            def twil(txt):
                from twilio.rest import Client 
                account_sid = 'ACba66e0e5fe42928da9057746e15bf777' 
                auth_token = 'c09637ed8319122d5e4bc2503d5c44ae' 
                client = Client(account_sid, auth_token)
                too = '98158160'

                message = client.messages.create(messaging_service_sid='MG6a60f5bedff96258f9921a6e7a290b8c', 
                                                body=txt,      
                                                to='+216'+too)
        
            text = msg.get(1.0, "end-1c")
            if 2<len(text)<100 and text!='type here.....':
                twil(text)
                forget(f4)
                after_snd.place(x=0,y=35)
                lbl5.place(x=0,y=0)
                txt_after.place(x=130,y=390)
                #contact_btn['state'] ='disabled'
                def lmbd():
                    messagebox.showinfo(title=None,message="You have the right to send only one message every time you open the application")
                contact_btn.config(command=lmbd)
                def callit():
                    home_btn.invoke()
                frm.after(3500, callit) 
            elif len(text)>100:
                messagebox.showerror(title=None,message='You can Send only 100 character')
                
            elif text =='type here.....' or len(text)<2:
                messagebox.showerror(title=None,message='Enter a Message')
                
            else :
                print('else it ')
        def returnit():
            if len(msg.get(1.0, "end-1c")) ==0:
        	    msg.insert("end",'type here.....') 
   
        f4.bind("<1>", lambda event: returnit())
        f1.bind("<1>", lambda event: returnit())
        lbl1.bind("<1>", lambda event: returnit())
        img_rv.bind("<1>", lambda event: returnit())
        msg_frm.bind("<1>", lambda event: returnit())
        f4.bind_all("<1>", lambda event:event.widget.focus_set())
        def do(e):
            snd_btn['image'] = snd_img2
            frm.update()
        def do2(e):
            snd_btn['image'] = snd_img1
            frm.update()
        snd_btn = Button(msg_frm,command=send_sms,image=snd_img1,bg=app_color,activebackground=app_color,bd=0)
        snd_btn.bind('<Enter>',do)
        snd_btn.bind('<Leave>',do2)

        fdback_lbl = Label(f1,text="Customer's FeedBack",bg=f1['bg'],bd=0,font=("Comic Sans MS", 50 , "bold"),fg='white')
    
        
        #places ===
        f1.place(x=0,y=0)
        msg_frm.place(x=750,y=140)
        lbl1.place(x=50,y=5)
        img_rv.place(x=0,y=0)
        imgs_frm.place(x=0,y=100)
        msg.place(x=7,y=70)
        snd_btn.place(x=145,y=370)
        fdback_lbl.place(x=290,y=0)
        el_lbl.place(x=80,y=205)
        el_lbl2.place(x=155,y=360)

    def backfrm():
    	info_frm['height']=516
    	info_frm['width']=890
    # images ====
    reviw_not = Image.open('apppng\\contactus\\rv.png')
    reviw_y = reviw_not.resize((700,200),Image.ANTIALIAS)
    reviw_img = ImageTk.PhotoImage(reviw_y)
    # ====
    snd_img1 = ImageTk.PhotoImage(file = 'apppng\\contactus\\snd-1.png')
    snd_img2 = ImageTk.PhotoImage(file = 'apppng\\contactus\\snd-2.png')
    #=====
    after_snd_n = Image.open('apppng\\contactus\\after-snd.png')
    after_snd_y = after_snd_n.resize((950,580),Image.ANTIALIAS)
    after_snd_img = ImageTk.PhotoImage(after_snd_y)
    #=====
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def onhover(widget,newmg,old):
        def hoverit(e):
            widget['image'] = newmg
        def back(e):
            widget['image'] = old
        widget.bind('<Enter>',hoverit)
        widget.bind('<Leave>',back)
        frm.update()
    info_frm = Frame(f4,bg='#cccccc',height=516,width=890)#height was 516

    logout_img1 = ImageTk.PhotoImage(file='apppng\\logout.png')
    logout_img2 = ImageTk.PhotoImage(file='apppng\\logout2.png')
    logout_btn = Button(f3,command=logout,image=logout_img1,bg='#0c1c34',bd=0,activebackground='#0c1c34')
    onhover(logout_btn,logout_img2,logout_img1)
    
    contact_img1 = ImageTk.PhotoImage(file='apppng\\contactus.png')
    contact_img2 = ImageTk.PhotoImage(file='apppng\\contactus2.png')
    contact_btn = Button(f2,command=contact,image=contact_img1,bg='#0c1c34',bd=0,activebackground='#0c1c34')
    onhover(contact_btn,contact_img2,contact_img1)
    
    home_img1 = ImageTk.PhotoImage(file='apppng\\home.png')
    home_img2 = ImageTk.PhotoImage(file='apppng\\home2.png')
    home_btn = Button(f3,command=home,image=home_img1,bg='#0c1c34',bd=0,activebackground='#0c1c34')
    onhover(home_btn,home_img2,home_img1)
    
    myacc_img1 = ImageTk.PhotoImage(file='apppng\\myaccount.png')
    myacc_img2 = ImageTk.PhotoImage(file='apppng\\myaccount2.png')
    myacc_btn = Button(f3,command=myacc,image=myacc_img1,bg='#0c1c34',bd=0,activebackground='#0c1c34')
    onhover(myacc_btn,myacc_img2,myacc_img1)
    
    home_btn.invoke()
    # places====================
    goall()
    f4.place(x=0,y=55)
    home_btn.place(x=0,y=0)
    myacc_btn.place(x=948,y=0)
    logout_btn.place(x=1125,y=0)
    contact_btn.place(x=0,y=0)#in the end == 1104
    frm.mainloop()
##################################################################### login def #############################################################################
def login():
	
    def sqllg():
        username = username_entry.get()
        password = password_entry.get()
        dbrun("USE easylife")
        check_username = dbget("SELECT username FROM users WHERE username = '%s'"%(str(username)))
        check_password = dbget("SELECT password FROM users WHERE password = '%s' AND username = '%s'"%(str(password),str(username)))
        if len(check_username)!=0 and len(check_password)!=0 and (len(username)!=0 and len(password)!=0):
            line2['fg'] = 'white'
            messagebox.showinfo(title=None,message='Login Successfully')
            f4.place_forget()
            back_button.place_forget()
            data_f = open('Data\\log.txt','w+')
            data_f.write(str(username)+'\n'+str(password))
            data_f.close()
            logs = open('Data\\logs.txt','w')
            if var_r.get() == 1:
            	logs.write('RMTRUE')
            elif var_r.get() == 0:
            	logs.write('RMFALSE')
            else :
            	pass
            logs.close()
            app()
        elif len(check_username)==0 and (len(username)!=0 and len(password)!=0):
            line1['fg'] = '#ff0033'
            messagebox.showerror(title=None,message='Wrong Username')
	            
        elif len(check_password)==0 and (len(username)!=0 and len(password)!=0):
            line2['fg'] = '#ff0033'
            line1['fg'] = 'white'
            messagebox.showerror(title=None,message='Wrong Password')
        else :
            messagebox.showerror(title=None,message='You Have To Give All The Information')
        
        	

        		
    bgall = '#0c1c34'
    logolb.place_forget()
    f1.place_forget()
    login_button.place_forget()
    singup_button.place_forget()
    f4 = Frame(frm,width=1270,height=540,bg=bgall)
    f4.place(x=14,y=80)
    # yellow frame =======
    yell_frm = Frame(f4,height=540,width=630,bg='white')#ffc107
    # logo head image ====
    head_not = Image.open('apppng\\logo_head.png')
    head_resized = head_not.resize((300,110),Image.ANTIALIAS)
    logo_head_image = ImageTk.PhotoImage(head_resized)
    logo_head_label = Label(f4,image=logo_head_image,bd=0,bg=bgall)
    # user image ===
    user_image = Image.open('apppng\\user.png')
    resized_user_image = user_image.resize((600,420),Image.ANTIALIAS)
    user_image_resized = ImageTk.PhotoImage(resized_user_image)
    #  mabel of user image
    user_image_label = Label(yell_frm,bg='white',image=user_image_resized)
    # def of going back to main page
    def back():
        f4.place_forget()
        logolb.place(x=5,y=180)
        f1.place(x=360,y=180)
        login_button.place(x=320,y=95)
        singup_button.place(x=320,y=190)
        back_button.place_forget()
    # go back button 
    back_image_button = Image.open('apppng\\back_button.png')
    resized_back_button = back_image_button.resize((45,35),Image.ANTIALIAS)
    back_image = ImageTk.PhotoImage(resized_back_button)
    back_button=Button(f3,image=back_image,bd=0,bg=f2['bg'],activebackground=f2['bg'],command=back)
    
    # user name label and entry // password label and entry
    line1 = Label(f4,text='___________________',font=('tahoma 25 bold'),fg='white',bd=0,bg=bgall)
    line2 = Label(f4,text='___________________',font=('tahoma 25 bold'),fg='white',bd=0,bg=bgall)
    username_label=Label(f4,text='Username',font=('Georgia',25,'bold'),bg=bgall,fg='white') #times  
    username_entry = Entry(f4,fg='white',width=43,bg=bgall,bd=0,font=('tahoma',12))
    password_label=Label(f4,text='Password',font=('Georgia',25,'bold'),bg=bgall,fg='white')
    password_entry = Entry(f4,show='*',fg='white',width=43,bg=bgall,bd=0,font=('tahoma',12))
    
    # show pass button ===
    # def to show password ===
    show_image = PhotoImage(file='apppng\\show.png')
    hidee_image = PhotoImage(file='apppng\\hide.png')
    def showpass():
        show_image = PhotoImage(file='apppng\\show.png')
        hidee_image = PhotoImage(file='apppng\\hide.png')
        if password_entry.cget('show') == '' :
            password_entry.config(show='*')
            show_pass.config(image=show_image)
            frm.mainloop()
        elif password_entry.cget('show') == '*' and password_entry.get() != '':
            password_entry.config(show='')
            show_pass.config(image=hidee_image)
            frm.mainloop()
    check_var = IntVar()
    show_pass = Button(f4,bd=0,bg=bgall,activebackground=bgall,image=show_image,command=showpass)
    # login button =======
    def hover(widget,new,old):
        def onit(e):
            widget['image']=new
        def out(e):
            widget['image']=old
        widget.bind('<Enter>',onit)
        widget.bind('<Leave>',out)
        frm.update()         
    login_go_image1 = ImageTk.PhotoImage(file='apppng\\logkey.png')#login_go_image_resized
    login_go_image2 = ImageTk.PhotoImage(file='apppng\\logkey2.png')
    login_go_button = Button(f4,image=login_go_image1,bg=bgall,bd=0,activebackground=bgall,command=sqllg)
    hover(login_go_button,login_go_image2,login_go_image1)
    # forgot password =======
    forgot_password_button = Button(f4,text='Forgot Password ?',fg='white',font=('Georgia 10 bold'),activeforeground='#ffc107',activebackground=bgall,bg=bgall,bd=0)
    # remember me next time ====
    var_r = IntVar()
    rmmbr = Checkbutton(f4, text = "Remember Me", variable = var_r, \
                 onvalue = 1, offvalue = 0,  \
                 font=("Georgia", 12, "bold"),bg=bgall,fg='#5e6ebe',activebackground=bgall,activeforeground='white')



    # places ==========================
    def loginpage():
        yell_frm.place(x=0,y=0)
        back_button.place(x=4,y=2)
        user_image_label.place(x=0,y=55)
         # logo head label==
        logo_head_label.place(x=800,y=5)
         # user and password ==
          # lines
        line1.place(x=759,y=182)
        line2.place(x=759,y=294)
        username_label.place(x=755,y=150)
        username_entry.place(x=760,y=193)
        password_label.place(x=755,y=260)
        password_entry.place(x=760,y=305)
         #showpass button ===
        show_pass.place(x=1075,y=340)
         # login button go ===
        login_go_button.place(x=870,y=440)
         # forgot password  ====
        forgot_password_button.place(x=755,y=340)
         # remember next time ====
        rmmbr.place(x=755,y=365)
    loginpage()
    frm.mainloop()

################################################################# singup def ################################################################################

from regexx import *
def singup():

    def sqll():
        global can_go
        email = email_get.get()
        username = username_get.get()
        password = password_get.get()
        phone_number = number_get.get()
        dbrun("USE easylife")
        dbrun("CREATE TABLE IF NOT EXISTS users (username varchar(250),password varchar(250),email varchar(250),phone BIGINT(255))")
        check = dbget("SELECT username FROM users WHERE username = '%s'"%(str(username)))
        check_email = dbget("SELECT email FROM users WHERE email = '%s'"%(str(email)))
        
        try :
            phone_number_new = phone_number.replace('+'+code,'')
            check_phone = dbget("SELECT phone FROM users WHERE phone = '%s'"%(str(phone_number_new)))
        except:
            messagebox.showwarning(title=None, message='Please Enter The Country')
            return

        # here check if the phone have only numbers
        only_number = phone_number_new.isnumeric()
        if only_number and len(phone_number_new) != 0:
        	pass
        elif len(phone_number_new) == 0:
        	pass
        else :
        	messagebox.showwarning(title=None,message='Use Only Numbers In Phone Number')
        	number_var.set('+'+code)
        	return

        global can_go
        can_pass = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','j','h','i','g','k','l','m','n','o','p','k','r','s','t','u','w','x','y','z','A','B','C','D','E','F','J','H','I','G','K','L','M','N','O','P','Q','R','S','T','W','X','Y','Z',]
        can_go=0
        if len(str(username))!= 0:
            def split(word): 
                    return list(word) 
            list_it = split(username)
            len_it = len(list_it)
            index_it = len_it - 1
            last_one = list_it[index_it]
            for x in list_it:
                for i in can_pass:
                    if x in can_pass:
                        if x == last_one:
                            can_go+=1
                            break
                        else:
                            continue	
                    else :
                        messagebox.showwarning(title=None,message="You Can't Use "+x+" In Username")
                        new_username = username.replace(x,'')
                        username_var.set(new_username)
                        break
                        
                else:
                    continue
                break
        else :
            can_go = 1
        ######################################kif l wifi yarja3 raja3 verify True ##############################################################################################################################################################################################
        is_valid = checkit(email)
        #validate_email(email,verify=False)
        if len(phone_number_new)>4 and can_go==1 and 8<=len(str(password))<=16 and len(check_phone)==0 and str(check) == '[]' and str(check_email)=='[]' and str(email) != '' and str(username)!= '' and str(password) != '' and is_valid == True and 4<=len(str(username))<=10:
            #}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}} pin box }}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
            def pinn():
                global x
                import PIL
                pin = str(randint(1954,9584))
                def speakit():
                    import win32com.client as w
                    speak = w.Dispatch('SAPI.SpVoice')
                    for i in pin:
                        speak.Speak(i)
                def send_button():
                    global x
                    get_pin = pin_entry.get()
                    if len(get_pin) > 4 or len(get_pin) < 4:
                        messagebox.showwarning(title=None, message='PIN Consists of 4 Numbers')
                        pin_var.set('')
                    elif str(get_pin) != str(pin) :
                        messagebox.showwarning(title=None, message='Wrong PIN')
                        pin_var.set('')
                    else :
                        root.destroy()
                        phone_number_new = phone_number.replace(code,'')
                        dbrun("insert into users VALUES('%s','%s','%s','%d')"%(str(username),str(password),str(email),int(phone_number_new)))
                        messagebox.showinfo(title=None,message='Done Now You Can Go And Login')
                        username_var.set('')
                        email_var.set('')
                        password_var.set('')
                        f4.place_forget()
                        back_button.place_forget()
                        login()
                        
                        
                from PIL import ImageTk,Image
                root = Tk()
                iconn = PhotoImage(file='apppng\\logo_head.png',master=root)
                root.iconphoto(False,iconn)
                root.geometry('400x300')
                root.resizable(False,False)
                root.title('')
                root.config(background='#1a0067')
                
                tk2label = Label(root,text='Click The Button And write The Pin',font=('tahoma 16 bold'),bg='#ffc107',fg='black')
                pin_button_image = ImageTk.PhotoImage(file='apppng\\button_pin.png',master=root)
                pin_button = Button(root,command=speakit,activebackground='#1a0067',image=pin_button_image,bd=0,bg='#1a0067')
                pin_var = StringVar()
                pin_entry = Entry(root,textvariable=pin_var,font=('tahoma 13'),bg='#16a9ff',bd=1,width=22)
                send_image = ImageTk.PhotoImage(master=root,file='apppng\\send_pin.png')
                send_button = Button(root,command=send_button,image=send_image,activebackground='#1a0067',bd=0,bg='#1a0067')
               

                tk2label.place(x=17,y=30)
                pin_button.place(x=130,y=80)
                pin_entry.place(x=99,y=180)
                send_button.place(x=130,y=240)
                
                root.mainloop()
            pinn()
        else :
             if can_go==1 and(str(email) == '' or str(password) == '' or str(username) == '' or len(phone_number_new) <4):
                 messagebox.showwarning(title=None, message='You Have To Give All The Information ')                 
             elif can_go==1 and str(check) != '[]':
                 messagebox.showwarning(title=None, message='This User Name Already Exists')
                 username_var.set('')
             elif can_go==1 and str(check_email) != '[]':
                 messagebox.showwarning(title=None, message='This Email Already Used')
                 email_var.set('')
             elif can_go==1 and is_valid != True :
                 messagebox.showwarning(title=None, message='This Email Not Exist')
                 email_var.set('')
             elif can_go==1 and (len(str(username)) < 4 or len(str(username)) > 10):
                 messagebox.showwarning(title=None,message="Please Enter Username Consists At Less From 4 letters And Don't Pass 10 Letters")
             elif can_go==1 and (len(str(password))>16 or len(str(password))<8):
                 messagebox.showwarning(title=None,message="Please Enter Password Consists At Less From 8 letters And Don't Pass 16 Letters")
             elif can_go == 0:
                pass
             elif len(check_phone)!=0:
             	messagebox.showwarning(title=None,message='This Number Already Used')
             	number_var.set('+'+code)
             elif len(phone_number_new) <4:
             	messagebox.showwarning(title=None,message='Please Give Phone Number')	 
             else : 
                 print('famma mochkel arja3 te3 sing up...')
    logolb.place_forget()
    f1.place_forget()
    login_button.place_forget()
    singup_button.place_forget()
    bgall = '#0c1c34'
    f4 = Frame(frm,width=1270,height=540,bg=bgall)
    f4.place(x=14,y=80)
    # def of going back to main page
    def back():
        f4.place_forget()
        logolb.place(x=5,y=180)
        f1.place(x=360,y=180)
        login_button.place(x=320,y=95)
        singup_button.place(x=320,y=190)
        back_button.place_forget()
    # go back button 
    back_image_button = Image.open('apppng\\back_button.png')
    resized_back_button = back_image_button.resize((45,35),Image.ANTIALIAS)
    back_image = ImageTk.PhotoImage(resized_back_button)
    back_button=Button(f3,image=back_image,bd=0,bg=f2['bg'],activebackground=f2['bg'],command=back)
    # frame of welcome ===========================
    f5 = Frame(f4,bg='#ffc107',width=630,height=540)
     # welcome image ================
    welcm_img_not = Image.open('apppng\\bon.png')
    wlcm_img_r = welcm_img_not.resize((630,540),Image.ANTIALIAS)
    wlcm_img = ImageTk.PhotoImage(wlcm_img_r)
     # wlcm image lebel =================
    wlcm_label = Label(f5,image=wlcm_img,bg=bgall)
     # signup lbl ======
    signup_image = PhotoImage(file='apppng\\signup_lbl.png')
    signup_lbl = Label(f4,image=signup_image,bd=0,bg=bgall)
     # username // email // password // cntr + number=======
    # def to show password ===
    show_image = PhotoImage(file='apppng\\show.png')
    hidee_image = PhotoImage(file='apppng\\hide.png')
    def showpass2():
        show_image = PhotoImage(file='apppng\\show.png')
        hidee_image = PhotoImage(file='apppng\\hide.png')
        if password_get.cget('show') == '' :
            password_get.config(show='*')
            show_pass2.config(image=show_image)
            frm.mainloop()
        elif password_get.cget('show') == '*' and password_var.get() != '':
            password_get.config(show='')
            show_pass2.config(image=hidee_image)
            frm.mainloop()
    check_var = IntVar()
    show_pass2 = Button(f4,bd=0,bg=bgall,activebackground=bgall,image=show_image,command=showpass2)
     # entrys ========
    number_var = StringVar()
    username_var = StringVar()
    email_var = StringVar()
    password_var = StringVar()
    fgallent = 'white'
    username_get = Entry(f4,textvariable=username_var,width=50,bg=fgallent,bd=1,font=('tahoma',13))
    email_get = Entry(f4,textvariable=email_var,width=50,bg=fgallent,bd=1,font=('tahoma',13))
    password_get = Entry(f4,show='*',textvariable=password_var,width=50,bg=fgallent,bd=1,font=('tahoma',13))
    number_get = Entry(f4,textvariable=number_var,width=22,bg=fgallent,bd=1,font=('tahoma',13))
    # cntr list 
    cntr_list = cntr_li
    def cntr(event):
        try:
            global code
            dlt = ["[","'","]","'"]
            name_of = cntr_get.get()
            country= CountryInfo(str(name_of))
            info = country.info()
            code = info['callingCodes']
            code = str(code)
            for i in dlt:
                code = code.replace(i,'')
                code = code.replace('[','')
                code = code.replace(']','')
            if len(name_of) != 0:
                number_var.set('')	
                number_var.set('+'+code)
        except KeyError:
            messagebox.showwarning(title=None,message='Pleas Enter The Phone Country Code Manually')  	     
    cntr_get = ttk.Combobox(f4,width=23,font=('tahoma',13),values=cntr_list,state='readonly')
    #cntr_get.current(0)#230 Tunisia
    cntr_get.bind("<<ComboboxSelected>>",cntr)
     # labels=========
    cntr_lbl = Label(f4,text='Country',fg='white',bg=bgall,font=('Georgia 15 bold'))
    number_lbl = Label(f4,text='Phone_Number',fg='white',bg=bgall,font=('Georgia 15 bold'))
    username_lbl = Label(f4,text='Username',fg='white',bg=bgall,font=('Georgia 15 bold'))
    email_lbl = Label(f4,text='Email',fg='white',bg=bgall,font=('Georgia 15 bold'))
    password_lbl = Label(f4,text='Password',fg='white',bg=bgall,font=('Georgia 15 bold'))
    # PASSWORD GENERATER =====================
     # def for generate a password ======
    def genps():
        abc = ['a','b','c','d','e','f','j','h','i','g','k','l','m','n','o','p','k','r','s','t','w','x','y','z']
        ABC = ['A','B','C','D','E','F','J','H','I','G','K','L','M','N','O','P','Q','R','S','T','W','X','Y','Z']
        num = ['1','2','3','4','5','6','7','8','9']
        ch = ['@','!','§','?']
        lengh = 10
        password = ''
        b = len(password)
        for i in range(lengh):
            if len(password) < lengh:
                password+=abc[random.randint(0,23)]
            if len(password) < lengh:
                password+=ABC[random.randint(0,23)]
            if len(password) < lengh:
                password+= num[random.randint(0,8)]
            if len(password) < lengh:
                password+= ch[random.randint(0,3)]
        password_var.set(password)
        f = open('password_'+str(username_get.get())+'.txt','w')
        f.write(password)
        f.close()
        messagebox.showinfo(title=None,message=('Your Password Is :\n'+str(password)))
     #===== make the image ==========
    #gen_button = Image.open('gn-ps.png')
    #gen_button = gen_button.resize((377,28),Image.ANTIALIAS)
    gen_pas_img = ImageTk.PhotoImage(file='apppng\\gn-ps.png',master=frm)
    gen_button = Button(f4,image=gen_pas_img,bg=bgall,command=genps,bd=0,activebackground=bgall)
    # signup button ====
     # open and resize imgae

    img_signup1 = ImageTk.PhotoImage(file='apppng\\signup_go.png')
    img_signup2 = ImageTk.PhotoImage(file='apppng\\signup_go2.png')
     # make the button
    sign_up_go = Button(f4,command=sqll,height=50,image=img_signup1,bg=bgall,bd=0,activebackground=bgall)
    def onit(e):
    	sign_up_go['image']=img_signup2
    def outit(e):
    	sign_up_go['image']=img_signup1
    sign_up_go.bind('<Enter>',onit)
    sign_up_go.bind('<Leave>',outit)   	
    # places ==========================
    def signuppage():
        back_button.place(x=4,y=2)
        
        f5.place(x=0,y=0)
        wlcm_label.place(x=0,y=0,relheight=1,relwidth=1)
        signup_lbl.place(x=830,y=0)

        xlbl = 710
        
        username_lbl.place(x=xlbl,y=90) 
        email_lbl.place(x=xlbl,y=180)
        number_lbl.place(x=960,y=265)
        cntr_lbl.place(x=xlbl,y=265)
        password_lbl.place(x=xlbl,y=350)
        
        
        username_get.place(x=730,y=120)
        email_get.place(x=730,y=210)
        cntr_get.place(x=730,y=295)
        number_get.place(x=980,y=295)
        password_get.place(x=730,y=380)
        show_pass2.place(x=1102,y=413)
        gen_button.place(x=730,y=413)
        
        sign_up_go.place(x=865,y=470)
    signuppage()

    frm.mainloop()
#####################################################################main page#######################################################################
frm.geometry('1300x700+150+100')
frm.resizable(False,False)
frm.title('EasyLife')

# == Image bg ====
#1 open image 1
image = Image.open('apppng\\bgdd.jpg')
# 2 resize 2
resized1 = image.resize((1300,700),Image.ANTIALIAS)
img = ImageTk.PhotoImage(resized1)
l1=Label(frm,image=img)
# == Logo ====
# 1 open image 1
logo = Image.open('apppng\\logo.png')
# 2 resize image 2
resized2 = logo.resize((350,350),Image.ANTIALIAS)
new_logo = ImageTk.PhotoImage(resized2)
logolb = Label(frm,image=new_logo,bd=0)
#icon photo ===
icon = PhotoImage(file='apppng\\logo.png')
frm.iconphoto(False,icon)
# ==  login / singin frame ===
f1 = Frame(frm,bg=app_color,width=934,height=350)
# creat login and sinup button in the frame f1
    # the login button 
login_png1 = ImageTk.PhotoImage(file='apppng\\login.png')
login_png2 = ImageTk.PhotoImage(file='apppng\\login2.png')
login_button = Button(f1,image=login_png1,bd=0,activebackground=app_color,bg=app_color,command=login)
    # the singup button
singup_png1 = ImageTk.PhotoImage(file='apppng\\singup.png')
singup_png2 = ImageTk.PhotoImage(file='apppng\\singup2.png')
singup_button = Button(f1,image=singup_png1,bd=0,activebackground=app_color,bg=app_color,command=singup)

def hover(widget,new,old):
	def init(e):
		widget['image'] = new
	def out(e):
		widget['image'] = old
	widget.bind('<Enter>',init)
	widget.bind('<Leave>',out)
hover(singup_button,singup_png2,singup_png1)
hover(login_button,login_png2,login_png1)

# info frame ==
f2 = Frame(frm,width=1300,height=40,bg=app_color)
f3 = Frame(frm,width=1300,height=42,bg=app_color)

def make_menu(w):
    global the_menu
    the_menu = Menu(w, tearoff=0,bg=app_color,relief=FLAT,fg='white',font=("Comic Sans MS", 14, "bold"),activeborderwidth=10,activeforeground='#6beadd',activebackground='#1a0067')
    the_menu.add_command(label="Cut")
    the_menu.add_command(label="Copy")
    the_menu.add_command(label="Paste")

def show_menu(e):
    w = e.widget
    the_menu.entryconfigure("Cut",
    command=lambda: w.event_generate("<<Cut>>"))
    the_menu.entryconfigure("Copy",
    command=lambda: w.event_generate("<<Copy>>"))
    the_menu.entryconfigure("Paste",
    command=lambda: w.event_generate("<<Paste>>"))
    the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)


make_menu(frm)


e1 =Entry()
e1.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

def mainpage():
    l1.place(x=0,y=0,relheight=1,relwidth=1)
    logolb.place(x=5,y=180)
    f1.place(x=360,y=180)
    login_button.place(x=320,y=95)
    singup_button.place(x=320,y=190)
    f2.place(x=0,y=660)
    f3.place(x=0,y=0)
#mainpage()

try :
	big_check = open('Data\\logs.txt','r')
except:
	mainpage()
big_check1 = big_check.readline()
if big_check1 == 'LOGEDOUT':
	mainpage()
elif big_check1 == 'RMTRUE' :
	app()
elif big_check1 == 'RMFALSE':
	mainpage()
else :
	mainpage()

frm.mainloop()
