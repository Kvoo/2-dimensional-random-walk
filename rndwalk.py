#rndwalk.py -- Simulates a 2-Dimensional random walk

from random import random
import math
from graphics import *


def intro():
    print("\nThis program simulates n steps on a 2-dimensional random walk")
    print("and outputs the end point.")

def open_window():
    win = GraphWin("2-Dimensional random walk", 500, 500)
    win.setCoords(-100, -100, 100, 100)
    win.setBackground("white")
    return win

def walk_n_steps(steps, win):
    point_x = 0
    point_y = 0
    for step in range(steps):
        x_new, y_new = walk_one_step(point_x, point_y)
        draw_line(win, point_x, point_y, x_new, y_new)
        point_x, point_y = x_new, y_new
    return point_x, point_y

def draw_line(win, point_x, point_y, x_new, y_new):
    step = Line(Point(point_x, point_y), Point(x_new, y_new))
    step.setWidth(2)
    step.setFill("black")
    step.draw(win)

def walk_one_step(point_x, point_y):
    angle = random() * 2 * math.pi
    point_x = point_x + math.cos(angle)
    point_y = point_y + math.sin(angle)
    return point_x, point_y

def output(steps, point_x, point_y):
    print("\nSteps simulated: {}".format(steps))
    print("Start point: 0, 0")
    print("End point: {}, {}\n".format(point_x, point_y))

def main():
    intro()
    win = open_window()
    steps = int(input("How many steps do you want to simulate? >> "))
    point_x, point_y = walk_n_steps(steps, win)
    output(steps, point_x, point_y)
    win.getMouse()

if __name__ == "__main__": main()
