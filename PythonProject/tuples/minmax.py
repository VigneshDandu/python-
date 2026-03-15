# Returning multiple values — very common in ML!
def min_max(numbers):
    return min(numbers), max(numbers)   # returns a tuple

low, high = min_max([3, 1, 9, 5])
print(low, high)   # 1 9