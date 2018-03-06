print("1 0 "*20)

n = int(input("Choose a number:"))
for i in range(n):
    if i % 2 == 0:
        print("1", end= " ")
    else:
        print("0", end= " ")
print()
