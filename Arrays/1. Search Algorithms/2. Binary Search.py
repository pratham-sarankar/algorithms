"""
Binary Search:
- Binary search is a search algorithm that finds the position of a target value within a sorted array.
- Binary search compares the target value to the middle element of the array.
- If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found.
- If the search ends with the remaining half being empty, the target is not in the array.
- Binary search runs in logarithmic time in the worst case, making O(log n) comparisons, where n is the number of elements in the array.

What is the complexity of binary search?
Ans. O(Log(n))
"""
def binary_search(arr, target):
    """
    Perform binary search on the given sorted array to find the target element.

    Parameters:
    - arr: Sorted list of elements to search through.
    - target: Element to search for.

    Returns:
    - If the target is found, return the index of the target in the array.
    - If the target is not found, return -1.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]
        if  mid_element == target:
            return mid 
        elif mid_element < target:
            low = mid + 1
        else: 
            high = mid - 1
    return -1       

# Example usage:
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_element = 9

result = binary_search(sorted_list, target_element)

if result != -1:
    print(f'Target element {target_element} found at index {result}.')
else:
    print(f'Target element {target_element} not found in the list.')