import random

jackpot = random.randint(1,100)

guess=int(input("Enter a number to guess:"))

counter = 1

while guess != jackpot:
    
    if guess<jackpot:
        print("Guess Higher Number")
    else:
        print("Guess The Lower Number:")

    guess=int(input("Enter a number to guess:"))
    
    counter+=1
    
else:
    print(" Congratulations You guessed correct number")
    print("You took total chances:", counter)
