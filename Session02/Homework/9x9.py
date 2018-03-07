for i in range(1, 10):
    for j in range(1, 10):
        if int(i*j) < 10:
            print("",int(i*j), end= " ")
        else:
            print(int(i*j), end= " ")
    print()

n = int(input("choose a number:"))
for a in range(1, n+1):
    for b in range(1, n+1):
        if int(a*b) < 10:
            print("",int(a*b), end= " ")
        else:
            print(int(a*b), end= " ")
    print()
