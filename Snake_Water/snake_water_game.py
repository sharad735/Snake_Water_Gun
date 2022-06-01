import random
def gamewin(comp,you):


# if two values are equal declare a tie
    if comp == you:
        return None
#checks all the possibilities if computer chooses 's'
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
#checks all the possibilities if computer chooses 'w'

    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
#checks all the possibilities if computer chooses 'g'

    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
    
         
    

while():  
    print("computer turn: snake(s),water(w) or gun(g)?")

    randno = random.randint(1,3)
    if randno == 1:
        comp = 's'
    elif randno == 2:
        comp = 'w'
    elif randno == 3:
        comp = 'g'
    you = input("Your turn: snake(s),water(w),or gun(g)?")
   
    a = gamewin(comp,you)
    print(f"computer choose {comp}")
    print(f"You choose {you}")
    if a == None:
        print("the game is a tie")
    elif a == False:
        print("you lose the game")
    else:
        print("you win the game")