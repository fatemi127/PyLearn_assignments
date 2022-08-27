import turtle
t = turtle.Turtle()
n = 30
for i in range (2,n): 
    num_sides = i+1
    side_length = 40
    angle = 360/ num_sides    
    for j in range(num_sides):
        t.forward(side_length)
        t.right(angle)

