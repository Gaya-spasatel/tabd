import math


def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def rectangle_area(a, b):
    return a * b


def circle_area(r):
    return math.pi * r ** 2


def pretty_result(figure_name, area):
    return {figure_name: area}


figures = ['rectangle', 'triangle', 'circle']

if __name__ == '__main__':
    figure_name = input('Enter figure name:')
    if figure_name in figures:
        area = 0
        if figure_name == figures[0]:
            print("Enter first side: ", end="")
            a = int(input())
            print("Enter second side: ", end="")
            b = int(input())
            area = rectangle_area(a, b)
        elif figure_name == figures[1]:
            print("Enter first side: ", end="")
            a = int(input())
            print("Enter second side: ", end="")
            b = int(input())
            print("Enter third side: ", end="")
            c = int(input())
            area = triangle_area(a, b, c)
        else:
            print("Enter radius: ", end="")
            r = int(input())
            area = circle_area(r)
        print(pretty_result(figure_name, area))
    else:
        print(f"Invalid input: {figure_name}")
