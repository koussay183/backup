from tkinter import messagebox
from tkinter import * 
def checkusername(username,usernamebox_var):
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
                    usernamebox_var.set(new_username)
                    
                    break
                        
            else:
                continue
            break
    else :
        can_go = 1
    return can_go

