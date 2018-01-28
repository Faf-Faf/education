"""
Seeker for perimeter and area of shapes
"""

import math

# Найти площадь и периметр круга; прямоугольника; квадрата; треугольника
#
# Найдем периметр и площать прямоугольника
# Pr = (a+b)*2
# Sr = a*b
# Найдем периметр и площадь треугольнка
# Pt = a+b+c
# St = a/(1/2)*h
# Найдем периметр и площадь круга
# Pc = (3.1415*2)*r
# Sc = 3.1415*r
# Найти периметр и площадь квадрата
# Ps = a*4
# Ss = a**2



def circle(r, per):
    """
    Find perimeter and square of a circle.

    r - radius
    per - flag to return a perimeter of the circle
          if false the square of the cirle returned

    return perimeter or square of the circle depending on per as a float
    """
    if per:
        res = 2 * math.pi * r
    else:
        res = math.pi * (r ** 2)
    return res



def rectangle(w, h, per):
    """
    Find perimeter and square of a rectangle.
    """
    if per:
        res = (w + h) * 2
    else:
        res = w * h
    return res



def triangle(a, b, c, per):
    """
    Find perimeter and square of a triangle.

    Add ivalid triangle edges sizes
    """
    if (a >= b + c or
        b >= a + c or
        c >= b + a):
        print("Invalid triangle edges sizes!")
        return -1

    if per:
        res = a + b + c
    else:
        p = (a + b + c) / 2
        res = (p * (p - a) * (p - b) * (p - c)) ** 0,5
    return res



def square(a, per):
    """
    Find perimeter and square of a square.
    """
    if per:
        res = a * 4
    else:
        res = a ** 2
    return res



def get_positive_num(prompt):
    """
    Understand are the number is positive and not equal to zero
    """
    num = -1
    while num <= 0:
        n = input(prompt)
        if n.isdecimal():
            num = float(n)
            if num <= 0:
                print("Positive number expecting.")
        else:
            print("Positive number expecting.")
    
    return num



def main():
    sc = input("Hello, please enter your shape code ([C]ircle, [R]ectangle, [T]riangle, [S]quare): ").upper()
    if sc == 'C':
        r = get_positive_num("Enter radius: ")
        print("Circle perimeter is", circle(r, True), "square is", circle(r, False))
    elif sc == 'R':
        w = get_positive_num("Enter width: ")
        h = get_positive_num("Enter high: ")
        print("Rectangle perimeter is", rectangle(w, h, True), "square is", rectangle(w, h, False))
    elif sc == 'T':
        a = get_positive_num("Enter a: ")
        b = get_positive_num("Enter b: ")
        c = get_positive_num("Enter c: ")
        print("Rectangle perimeter is", triangle(a, b, c, True), "square is", triangle(a, b, c, False))
    elif sc == 'S':
        a = get_positive_num("Enter a: ")
        print("Rectangle perimeter is", square(a, True), "square is", square(a, False))
    else:
        print("Invalid shape code [", sc, "]")


main()