# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     rgb_colors.append((r, g, b))
# import random
# import turtle
# from turtle import Turtle, Screen
#
# dot = Turtle()
# dot.shape("turtle")
# turtle.colormode(255)
# colors = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
# dot.width(20)
# dot.penup()
# go_to_x = -300
# go_to_y = -300
# dot.goto(go_to_x, go_to_y)
#
# while go_to_x < 300:
#     for _ in range(10):
#         dot.pendown()
#         dot.color(random.choice(colors))
#         dot.dot(20)
#         dot.penup()
#         dot.forward(50)
#         dot.pendown()
#     go_to_y += 50
#     dot.penup()
#     dot.goto(go_to_x, go_to_y)
#
#
# screen = Screen()
# screen.exitonclick()

s = ["h","e","l","l","o"]
temp = ''
for num, val in enumerate(s):
    temp += val

for i in reversed(temp):
    s.append(i)

print(s)