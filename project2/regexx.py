import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def checkit(email):  
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex,email)):  
        return True              
    else:  
        return False
    

