# alias python='winpty python'
import turtle
import random
colors = ["black", "green", "red", "blue", "purple"]


def spiral(sides, turn, color, width):
    t = turtle.Turtle()
    t.color(color)
    t.width(width)
    t.speed(0)
    for n in range(sides):
        t.forward(n)
        t.right(turn)


for number in range(10):
    print("Wanna see some spirals?/n")
    Spiral_req = input("Then type in 1, in order to quit type 0/n")
    # print("You typed in:", Spiral_req, "!")
    if Spiral_req == "1":
        # print("You're in the loop!")
        angle = random.randint(70, 340)
        color = random.choice(colors)
        spiral(200, angle, color, 1)
    else:
        quit
        # print("Loop aborted!")
