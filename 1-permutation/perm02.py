def heap_permutations(data, k):
  if k == 1: #yes
    print(data) #[1,2,3]
    return
  for i in range(k):
    heap_permutations(data, k-1) #data, 2
    if k%2 == 0:
      data[i], data[k-1] = data[k-1], data[i] #[2,1,3]
    else:
      data[0], data[k-1] = data[k-1], data[0]
      
elements= [1,2,3]
heap_permutations(elements, len(elements))