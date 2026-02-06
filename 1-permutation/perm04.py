'''
how_many = 0

for i in range(10000, 99999 + 1):
  if i%2 == 1:
    set_of_digits = set(str(i))
    if set_of_digits.issubset({'0', '1', '2', '3'}):
      how_many +=1

print(how_many)

'''
from random import randint

successes = 0

n = 10**7
for i in range(n):
  a = randint(1,6)
  b = randint(1,6)
  if a + b in {4, 5, 6}:
    successes += 1

p = successes / n

print(f"Probability is: {p*100:.2f}%")