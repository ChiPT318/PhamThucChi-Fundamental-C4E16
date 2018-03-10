for i in range(1, 11):
    if i % 2 == 0:
        for j in range(1, 11):
            if j % 2 == 0:
                print("1 ", end= "")
            else:
                print("0 ", end= "")
    else:
        for j in range(1, 11):
            if j % 2 == 0:
                print("0 ", end= "")
            else:
                print("1 ", end= "")
    print()

n = int(input("Choose a number:"))
for i in range(1, n+1):
    if i % 2 == 0:
        for j in range(1, n+1):
            if j % 2 == 0:
                print("1 ", end= "")
            else:
                print("0 ", end= "")
    else:
        for j in range(1, n+1):
            if j % 2 == 0:
                print("0 ", end= "")
            else:
                print("1 ", end= "")
    print()

# Cach 2: thu i+j de phan biet 1, 0
