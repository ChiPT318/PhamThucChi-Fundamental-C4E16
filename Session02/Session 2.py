# a = int(input("side"))
# print("*"*a)
# for i in range(a+1):
#     print(" "*int(a-i),"*")
# print("*"*a)
for i in range(6):
    for j in range(6):
        if j >= 6 - i:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
