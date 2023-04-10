import random
n=random.randrange(0,100)
while True:
    guess=int(input("enter your guess: "))
    if guess==n :
        print("equal")
        break
    elif guess<n :
        print("n is bigger")
    else :
        print("n is smaller")