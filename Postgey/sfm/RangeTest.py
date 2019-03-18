print(list(range(0, 10)))
l = [x * x for x in range(0, 11)]
print(l)
g = (x * x for x in range(10))
for n in g:
    print(n)

for x in range(10):
    print(x)
