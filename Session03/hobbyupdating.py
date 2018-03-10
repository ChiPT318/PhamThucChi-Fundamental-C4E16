menu = ["rau muong","ca vien chien","pho","suon xao","rau","thit"]

for i in range(len(menu)):
    print(i+1,". ", menu[i], sep="")

pos = int(input("Position you want to update?"))
print(menu[pos-1])
new = input("Replacement?")
menu[pos-1] = new
for index, menu in enumerate(menu):
    print(index+1, ". ", menu, sep="")
