store = ["t-shirt", "sweater"]
print(*store, sep=", ")
n = input("What else?")
store.append(n)
print(*store, sep=", ")
pos = int(input("Update position:"))
new = input("New item:")
store[pos-1] = new
print(*store, sep=", ")
pos1 = int(input("Delete position: "))
del store[pos1-1]
print(*store, sep=", ")
