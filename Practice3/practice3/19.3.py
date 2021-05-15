import math
def roots_of_quadratic_equation(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 =(-b - math.sqrt(discr)) / (2 * a)
        return x1,x2
    elif discr == 0:
        x = -b / (2 * a)
        return x
    else:
        return 0

result = roots_of_quadratic_equation(1, -3, 2)
print(*sorted(result))