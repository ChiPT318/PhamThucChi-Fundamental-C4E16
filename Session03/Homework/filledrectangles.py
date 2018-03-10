from turtle import*
speed(-1)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(5):
    color(colors[i-5])
    begin_fill()
    for j in range(1, 5):
        if j % 2 == 1:
            forward(50)
            right(90)
        else:
            forward(80)
            right(90)

    forward(50)
    end_fill()

mainloop()
