f = abs
print(f(-10))


def add(x, y, f):
    return f(x) + f(y)


print(add(10, -10, abs))


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8])
print(list(r))


def findMinAndMax(list1):
    if len(list1) == 0:
        return None, None
    max_value = list1[0]
    min_value = list1[0]
    for i in list1:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i

    return min_value, max_value


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败1!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败3!')
else:
    print('测试成功!')
