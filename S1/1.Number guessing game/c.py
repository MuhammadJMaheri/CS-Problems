'''module for generating random variables'''
import random

n=random.randrange(0,100)
i=0

while i<10:
    guess=int(input("enter your guess: "))
    i=i+1

    if guess==n :
        print("equal")
        break
    if guess<n :
        print("n is bigger")
    else :
        print("n is smaller")
