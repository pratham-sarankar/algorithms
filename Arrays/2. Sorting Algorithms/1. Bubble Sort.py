"""
Bubble Sort: 
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

Steps:
1. Traverse through the array and compare the adjacent elements in pairs.
2. If the element on the left is greater than the element on the right, swap the two elements.




What is the complexity of Bubble Sort?
Ans. O(n^2) in the worst case and O(n) in the best case
"""
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            break

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)

print("Sorted array:", my_list)  