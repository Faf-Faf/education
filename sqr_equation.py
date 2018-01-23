"""
Square equation solver
"""

import math
# ax^2 + bx + c = 0
#
# D = b^2 - 4ac
#
# Если Д == 0, то корень 1.
# Если Д < 0, то корней нет.
# Если Д > 0, то 2 корня.
#
# Х1,2 = (-b ± √D)/2a
#

def se_solver(a, b, c):
    """
    Solves square equation

    a, b, c - coeffitients of the equation

    returns (x1, x2) or (x1) or None if the equation has no solution
    """
    
    # Вычисляем дискриминант (Д).
    d = b*2 - 4*a*c
    # Если Д меньше нуля, то возвращаем None.
    if d < 0:
        return None
    # Если Д равно нулю, то возвращаем 1 корень.
    if d == 0:
        return ( -b/(2*a) )
    # Если Д больше нуля, то вычисляем оба корня и возвращаем их.
    x1 = (-b - math.sqrt(d))/(2*a)
    x2 = (-b + math.sqrt(d))/(2*a)
    
    return ( x1, x2 )



def main():
    print("Square equation solving program.")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    res = se_solver(a, b, c)
    if res == None:
        print("There is no solution for the equation.")
        return
    
    if len(res) == 1:
        print("There is only one root", res[0])
    else:
        print("Root #1", res[0], ", root #2", res[1])


main()
