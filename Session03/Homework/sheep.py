#2.1
flock = [5, 7, 300, 90, 24, 50, 75]
print("My name is Chi and this is my flock:", flock)

#2.2

fattie = flock[0]
count = 0
while count < len(flock):
    for i in range(len(flock)):
        if fattie >= flock[i]:
            fattie = fattie
        else:
            fattie = flock[i]
        count += 1

print("Now my biggest sheep has size ", fattie, " let's shear it")

#2.3
flock[flock.index(fattie)] = 8
print("After shearing here is my flock:", flock)

#2.4
for i in range(len(flock)):
    flock[i] = flock[i] + 50
print("One month has passed, here is my flock now:", flock)
