hobbies = ["youtube", "food", "sleep"]
print(*hobbies, sep=", ")
n = input("What elso do you like?")
hobbies.append(n)
print(*hobbies, sep=", ")
