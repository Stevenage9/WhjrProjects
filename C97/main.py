import random
num=random.randint(0,9)
chances=0
while chances<5:
    uin=int(input("Your guess is: "))
    if uin==num:
        print("Correct! The number was ",num,"!")
        input("Press any key to exit ")
        break
    elif uin<num:
        print("WRONG! You guessed too low!")
    elif uin>num:
        print("WRONG! You guessed too high!")
    chances=chances+1
if not chances < 5:
    print("You didnt guess right! The number was ",num,"!")