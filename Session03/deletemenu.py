menu = ["rau muong","ca vien chien","pho","suon xao","rau","thit"]
for index, item in enumerate(menu):
    print(index+1, ". ", item, sep="")

position = int(input("Remove the following"))
# print(menu[position -1])

del menu[position - 1] #del theo index
print(menu)
# remove - theo item
# pop- tu tra
