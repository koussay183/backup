import random
number = random.randint(1,99)
def n():
    n = int(input('Enter a number between 1 and 99 :'))
        
    if n < number :
            
        print(n,'< number ')
    elif n > number:
        print(n,'> number')
    else :
        print('You Win')
print('==== Gess It Win It ====')

while n != number :
    n()
    
    


