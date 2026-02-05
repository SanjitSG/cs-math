from itertools import permutations
from math import factorial
from collections import defaultdict

# perm = [''.join(x) for x in list(permutations("barbarian"))]
#perm = {''.join(x) for x in list(permutations("electrocardiagraphic"))} #set {} notation to eliminate the repetition
#print(perm)
#print(len(perm))


def how_many_permutations(text: str) -> int:
  letters = defaultdict(int)
  for letter in text:
      letters[letter] += 1
   
  numerator = factorial(len(text))
  factors = [factorial(count) for count in letters.values()]
  denominator = 1
  for factor in factors:
    denominator *= factor
  return numerator // denominator

print(how_many_permutations("electrocargafiographic"))
#print(list(map(''.join, permutations("ab"))))

#print(factorial(9))