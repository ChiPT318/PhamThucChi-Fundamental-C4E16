

from turtle import *

n = input("How many angles?")
a = int(n)

shape("turtle")
speed(-1)

#filling color

fillcolor("blue")
begin_fill()
for i in range (a):
# draw a square

    forward(100)
    left(360/a)

end_fill()    
mainloop()
