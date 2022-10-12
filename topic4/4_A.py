a, b = map(int, input().split())
d = a // b
r = a % b
f = format(a / b, '5f')
print(d, r, f)