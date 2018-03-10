# from random import randint
# n = (randint(0,100))
playing = True
count = 0
while True:
    m = int(input("Guess a number"))
    if n == m:
        print("Bingo")

    elif n > m:
        print("Too small")
    else:
        print("Too large")
    count =+ 1
    if count == 7:
        print("you lost")
        playing = False
