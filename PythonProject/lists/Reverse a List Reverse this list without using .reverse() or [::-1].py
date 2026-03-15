items = [10, 20, 30, 40, 50]

print("Original:", items)

i = 0
j = len(items) - 1

while i < j:
    # Swap items at positions i and j
    items[i], items[j] = items[j], items[i]
    i += 1
    j -= 1

print("Reversed:", items)
