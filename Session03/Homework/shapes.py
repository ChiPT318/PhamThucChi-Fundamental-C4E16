from turtle import*
speed(1)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(3,8):
    color(colors[i-3])
    n = int(((i-2)*180)/i)
    left(n)
    for j in range(i):
        forward(100)
        right(180-n)
    right(n)

mainloop()
