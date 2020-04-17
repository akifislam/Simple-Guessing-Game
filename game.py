#Akif Islam Super Beginner Project
from random import randint

print("***Guessing Game with Python ! ***\n")

magic_number = randint(0,100) #Select your range #Here is 0 to 100
chances=5; #How Many Chances?


while(chances!=0) :

    user_input = int(input("\nEnter Your Guess :  "))


    if(user_input==magic_number) :
        print("Congratulations ! You are a mind reader !")
        break

    elif(user_input>magic_number) :
        print("Try Smaller Number !")
    else:
        print("Try Bigger Number!")

    chances -= 1;
    print(f"Chances left : {chances}")

if chances==0 :
    print(f"Sorry ! The number was {magic_number} ")
    print("Run this Program Again !")
else :
    print("Thanks for playing !")




