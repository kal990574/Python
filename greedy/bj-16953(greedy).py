A,B = map(int, input().split())
##again
count = 1
while True:
  if A == B:
    break
  elif (B % 2 != 0 and B % 10 != 1) or (A > B):
    count = -1
    break
  else:
    if B % 10 == 1:
      B //= 10
      count += 1
    else:
      B //= 2
      count += 1
print(count)
