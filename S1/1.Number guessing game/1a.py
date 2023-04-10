import random
n=random.randrange(0,100)
guess=int(input('enter your guess:'))
if(guess==n):
    print('equal')
elif(guess>n):
    print('n is smaller')
else:
    print('n is greater')
