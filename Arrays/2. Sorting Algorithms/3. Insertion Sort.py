def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i-1

        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Example usage:
my_array = [5, 2, 4, 3, 1]
insertion_sort(my_array)
print("Sorted array:", my_array)