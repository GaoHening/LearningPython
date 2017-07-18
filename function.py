import math
print(abs(-100))
n1 = 255
n2 = 1000
print(hex(n1), hex(n2))


def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x1, y1 = move(100, 100, 60, math.pi/6)
print(x1, y1)


def quadratic(a, b, c):
    r1 = (b*(-1)+math.sqrt(b*b-4*a*c))/(2*a)
    r2 = (b*(-1)-math.sqrt(b*b-4*a*c))/(2*a)
    return r1, r2
print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))


