n = int(input())
rooms = [[[0 for x in range(10)] for y in range(3)] for z in range(4)]
for i in range(n):
  b, f, r, v = map(int, input().split())
  rooms[b - 1][f - 1][r - 1] += v

for z in range(4):
  for y in range(3):
    print(" " + " ".join(map(str, rooms[z][y])))
  if z != 3:
    print('#' * 20)
