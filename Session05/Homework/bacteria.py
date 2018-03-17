b = int(input("How many B bacteria is there? "))
t = int(input("How much time in minutes do we wait? "))
number = b * 2**(t%2)
print("After ", t, " minutes, we would have", number, " bacteria")
