while True:
  x, y = map(int, input().split())
  list = sorted([x, y])
  if list[0] == 0 and list[1] == 0:
    break
  print(list[0], list[1])