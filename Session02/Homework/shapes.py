from turtle import*
speed(1)
for i in range(3,7):
    if i % 2 == 0:
        color("red")
    else:
        color("blue")

    n = int(((i-2)*180)/i)
    left(n)
    for j in range(i):
        forward(100)
        right(180-n)
    right(n)

mainloop()
