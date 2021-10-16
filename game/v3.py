from random import*
from gtts import gTTS
import os


cbs = []
jscore = 0
oscore = 0

name = input('ENTER YOUR NAME :')

choise = input('choise pair  ==> p or impair ==> i :')
while choise != 'p' and choise != 'i' :
    choise = input('choise pair  ==> p or impair ==> i :')


def game1():
    w = False
    l = False
    global jscore
    global oscore

    try :
        num_1 = int(input('ENTER THE NUMBER YOU CHOISE :'))
        while num_1 > 5 or num_1 < 0 :
            num_1 = int(input('ENTER THE NUMBER YOU CHOISE :'))
    except ValueError :
        print('you can''t enter a float number try again ....')
        num_1 = int(input('ENTER THE NUMBER YOU CHOISE :'))
    #her pc will choise a number
    num_2 = randint(0,5)
    cbs.append([num_1,num_2])
    #cbs.append(num_2)
    #calc
    ruselt = num_1 + num_2

    if ((ruselt % 2 ) == 0 and choise == 'p') or ((ruselt % 2 ) != 0 and choise == 'i') :
        w = True 
        print("pc num ===> " + str(num_2)  +" <===")
        print(name ,"num ===> " + str(num_1) +" <===")
        print("ruselt = " + str(ruselt) + ' so you win')
    else :
        l = True 
        print("pc num ===> " + str(num_2)  +" <===")
        print(name ,"num ===> " + str(num_1) +" <===")
        print("ruselt = " + str(ruselt) + ' so you lose ' )
    if w == True :
            jscore += 1
                
    elif l == True :
            oscore +=1
        
    print("PC SCORE = ",oscore,'        ',"YOUR SCORE =",jscore)    
#game1()
def game2():
    for i in range(19):
        print("=====================================")
        i = game1()
        if jscore == 10 :
            print(name,'win ..... score = ',jscore , '    pc score = ',oscore)
            wna = True
            return wna 
            break
        elif oscore == 10 :
            print("pc win ..... score = ",oscore,'      ',name,' score = ',jscore)
            wna = False
            return wna
            break
        
     

pff = game2()

def wnaa(x):
    for i in cbs:
        print(i)
    #if x == True :
    #    mytext = name+'you are the winner'
    #elif x == False:
    #    mytext =name+'you lose try next time maybe you will win'
    #language = 'en'
    #output = gTTS(text=mytext,lang=language,slow=False)
    #output.save("go.mp3")
    #os.system('start go.mp3')
wnaa(pff)
        
input()



