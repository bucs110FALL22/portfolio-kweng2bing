import random

n = random.randrange(1,100)
count = 0
upper_limit = 20
iters = {}
max_so_far = 0
print(n)
while n != 1:
  if n % 2 == 0:
    n = n//2
  else:
    n = 3*n + 1
  print(n)
  count += 1
  if count >= 2 and count <= upper_limit:
    iters[count] = n
  if max_so_far < count:
    max_so_far = count
print(iters)