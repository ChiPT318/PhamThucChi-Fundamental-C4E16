flock = [5, 7, 300, 90, 24, 50, 75]
fattie = flock[0]
count = 0
while count < len(flock):
    for b in range(len(flock)):
        if fattie >= flock[b]:
            fattie = fattie
        else:
            fattie = flock[b]
        count += 1
flock[flock.index(fattie)] = 8
print("After shearing here is my flock:", flock)
for a in range(3):
    print("MONTH ", a+1)
    for i in range(len(flock)):
        flock[i] = flock[i] + 50
    print("One month has passed, here is my flock now:", flock)
    if a == 2:
        break

    else:
        fattie1 = flock[0]
        count = 0
        while count < len(flock):
            for j in range(len(flock)):
                if fattie1 >= flock[j]:
                    fattie1 = fattie1
                else:
                    fattie1 = flock[j]
                count += 1

            print("Now my biggest sheep has size ", fattie1, " let's shear it")
            flock[flock.index(fattie1)] = 8
            print("After shearing here is my flock:", flock)

total = 0
for n in range(len(flock)):
    total += flock[n-1]
print("My flock has in size totoal:", total)
print("I would get", total, "* 2$ = ", total*2,"$")
