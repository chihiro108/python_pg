import math
r = float(input())
Square = format((r ** 2) * math.pi, '6f')
Circumference = format(2 * r * math.pi, '6f')
print(Square, Circumference)