import math
from collections import Iterable

age = 10
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# sum1 = 0
# for x in range(100):
#     print(x)

d = {'Michael': 95, 'Bob': 100, 'Tracy': 85}
print(d['Michael'])
d.get('Tracy')

print(isinstance('abc', Iterable))
