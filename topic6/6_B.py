n = int(input())
marks = ['S', 'H', 'C', 'D']
trumps = [[mark, number] for mark in marks for number in range(1, 14)]
list_1 = []
for i in range(1, n + 1):
  mark, number = map(str, input().split())
  number = int(number)
  list_1.append([mark, number])

for n in list_1:
  for k in trumps:
   if n == k:
     trumps.remove(n) 

for mark, number in trumps:
    if mark == 'S':
      print(mark, number)
    if mark == 'H':
      print(mark, number)
    if mark == 'C':
      print(mark, number)
    if mark == 'D':
      print(mark, number)
