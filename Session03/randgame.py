from random import randint
n = (randint(0,100))
loop = True
while True:
    m = int(input("Guess a number"))
    if n == m:
        print("Bingo")
        break
    elif n > m:
        print("Too small")
    else:
        print("Too large")
