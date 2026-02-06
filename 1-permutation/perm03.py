def heap_permutations(data, k):
    if k == 1:
        print(f"  FOUND: {data}")
        return

    for i in range(k):
        heap_permutations(data, k - 1)
        
        # Determine which index to swap with the last element (k-1)
        swap_index = i if k % 2 == 0 else 0
        
        if i < k - 1: # Only swap if there are iterations left
            print(f"  Swapping indices {swap_index} and {k-1}: {data[swap_index]} <-> {data[k-1]}")
            
            # Perform the swap
            data[swap_index], data[k - 1] = data[k - 1], data[swap_index]
            
            # Show the result of the swap
            visualize_swap(data, swap_index, k - 1)

def visualize_swap(data, idx1, idx2):
    """Helper to print the list with arrows pointing to swapped indices."""
    list_str = str(data)
    # Basic alignment for arrows
    pointers = [" "] * len(list_str)
    
    # Estimate positions of elements in the string representation
    # This works best for single-digit integers
    items = list_str.replace('[', '').replace(']', '').split(', ')
    pos = 1
    for i, item in enumerate(items):
        if i == idx1 or i == idx2:
            print(f"  {list_str}")
            arrow_line = [" "] * len(list_str)
            # Simple logic to place '^' under the numbers
            # (Roughly finding the index in the string)
            target = list_str.find(item) if i == 0 else list_str.find(item, pos)
            arrow_line[target] = "^"
            # Repeat for second index
            other_idx = idx2 if i == idx1 else idx1
            other_item = items[other_idx]
            target2 = list_str.find(other_item)
            arrow_line[target2] = "^"
            print("  " + "".join(arrow_line))
            break
    print("-" * 30)

elements = [1, 2, 3, 4]
print(f"Starting with: {elements}\n" + "="*30)
heap_permutations(elements, len(elements))