#this programme generate a passwords from weak to strong
import random
choise = input('weak or normal or strong :')
while choise != 'weak' and choise != 'normal' and choise != 'strong':
    print('please enter one of the type above')
    choise = input('weak or normal or strong :')
lengh = int(input('enter lengh :'))
while lengh <=0 :
    try:
        print('lengh need to be > 0')
        lengh = int(input('enter lengh :'))
    except ValueError:
        print('lengh need to be > 0')
        lengh = int(input('enter lengh :'))


abc = ['a','b','c','d','e','f','j','h','i','g','k','l','m','n','o','p','k','r','s','t','w','x','y','z']
ABC = ['A','B','C','D','E','F','J','H','I','G','K','L','M','N','O','P','Q','R','S','T','W','X','Y','Z']
num = ['1','2','3','4','5','6','7','8','9']
ch = ['@','!','§','?']

password = ''
b = len(password)
if choise == 'weak':
    for i in range(lengh):
        password+=abc[random.randint(0,23)]
    
elif choise == 'normal':
    for i in range(0,lengh//2):
        password+=abc[random.randint(0,23)]
        password+=ABC[random.randint(0,23)]
elif choise == 'strong':
    for i in range(lengh):
        if len(password) < lengh:
            password+=abc[random.randint(0,23)]
        if len(password) < lengh:
            password+=ABC[random.randint(0,23)]
        if len(password) < lengh:
            password+= num[random.randint(0,8)]
        if len(password) < lengh:
            password+= ch[random.randint(0,3)]
        else :
            break #new

print('==========')        
print(password)
print(choise)
print('==========')
input()
    
