from itertools import combinations

while True:
 n, x = map(int, input().split())
 list = range(1, n + 1)
 count = 0
 if n == 0 and x == 0:
   break
 for i in combinations(list, 3):
   if sum(i) == x:
     count += 1
 print(count)
