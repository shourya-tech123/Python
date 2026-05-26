import random
attemps=0
computer=random.randint(1, 50)
while attemps<=5:
    c =int(input("Enter any no between 1 to 50: "))
    if c==computer:
        print("You have won the game")
    elif c>computer:
        print("The secret no. is smaller than the no. provided ")
    elif c<computer:
        print("The secert no. is greater than the no. provided ")
    attemps+=1
    
    