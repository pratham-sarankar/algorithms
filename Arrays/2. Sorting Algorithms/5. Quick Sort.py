def quick_sort(arr: list):
    n = len(arr)
    if n <= 1:
        return arr.copy()
    
    lower = []
    higher = []

    pivot = arr.pop()

    for item in arr:
        if item < pivot:
            lower.append(item)
        else:
            higher.append(item)
    
    return quick_sort(lower) + [pivot] + quick_sort(higher)

# Example usage:
my_array = [5, 2, 4, 3, 1]
print("Sorted array:", quick_sort(my_array))