from itertools import permutations

#perm = [''.join(x) for x in list(permutations("barbarian"))]
perm = {''.join(x) for x in list(permutations("barbarian"))} #set {} notation to eliminate the repetition
print(perm)
print(len(perm))