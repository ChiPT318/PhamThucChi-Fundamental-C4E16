store = ["t-shirt", "sweater"]
n = input("What do you want?")
if n == "R":
    print(*store, sep=", ")
elif n == "C":
    new = input("What else")
    store.append(new)
    print(*store, sep=", ")
elif n == "U":
    pos = int(input("Update position:"))
    new = input("New item:")
    store[pos-1] = new
    print(*store, sep=", ")

elif n == "D":
    pos1 = int(input("Delete position: "))
    del store[pos1-1]
    print(*store, sep=", ")
