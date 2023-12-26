"""
What is the complexity of Selection Sort?
Ans. The complexity is O(n^2) in all cases because algorithm involves nested loops, where the outer loops runs for n iterations and the inner loops runs for (n-1),(n-2)...,2,1 iterations in successive passes.
"""

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i 
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Example usage:
my_list = [64, 25, 12, 22, 11]
selection_sort(my_list)

print("Sorted array:", my_list)