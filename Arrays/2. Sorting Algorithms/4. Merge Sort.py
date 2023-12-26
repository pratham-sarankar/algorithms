def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(right, left)

def merge(right, left):
    arr = []
    i,j = 0,0
    while i < len(left) and j<len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else: 
            arr.append(right[j])
            j += 1
    arr.extend(left[i:])
    arr.extend(right[j:])
    return arr

# Example usage:
my_array = [5, 2, 4, 3, 1]
print("Sorted array:", merge_sort(my_array))