from random import *
def game1():

    
    #here will choise name 
    name = input('ENTER YOUR NAME :')

    #here will choise zawji or fardi

    choise = input('choise pair  ==> p or impair ==> i :')
    while choise != 'p' and choise != 'i' :
       choise = input('choise pair  ==> p or impair ==> i :') 

    #here will choise number
    try :
        num_1 = int(input('ENTER THE NUMBER YOU CHOISE :'))
        while num_1 > 5 or num_1 < 0 :
            num_1 = int(input('ENTER THE NUMBER YOU CHOISE :'))
    except ValueError :
        print('you can''t enter a float number try again ....')
        num_1 = int(input('ENTER THE NUMBER YOU CHOISE :'))
    #her pc will choise a number
    num_2 = randint(0,5)

    #calc
    ruselt = num_1 + num_2

    if ((ruselt % 2 ) == 0 and choise == 'p') or ((ruselt % 2 ) != 0 and choise == 'i') :
         
        print("pc num ===> " + str(num_2)  +" <===")
        print("your num ===> " + str(num_1) +" <===")
        print("ruselt = " + str(ruselt) + ' so you win')
    else :
        
        print("pc num ===> " + str(num_2)  +" <===")
        print("your num ===> " + str(num_1) +" <===")
        print("ruselt = " + str(ruselt) + ' so you lose ' )
game1()
