import turtle
import random


def estimate_pi(iterations):
    turtle.penup()
    turtle.speed(0)

    darts_in = 0
    darts_total = 0

    for iteration in range(iterations):
        y_coordinate = random.uniform(-1, 1)
        x_coordinate = random.uniform(-1, 1)

        if (((x_coordinate ** 2) + (y_coordinate ** 2)) ** 0.5) <= 1:
            color = "green"
            darts_in = darts_in + 1
            darts_total = darts_total + 1

        else:
            color = "red"
            darts_total = darts_total + 1

        turtle.setpos(x_coordinate * 150, y_coordinate * 150)
        turtle.dot(5, color)

    pi_approx = 4 * (darts_in / darts_total)

    print("Pi is approximately: {0:.4f}".format(pi_approx))

    turtle.done()


if __name__ == '__main__':
    estimate_pi(250)
