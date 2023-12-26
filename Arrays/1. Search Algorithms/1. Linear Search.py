"""
1. Linearly traverse through the array and at each step check if the current element is equal to the target element, if yes, return the index of the current element. If the target element is not found, return -1.

What is the complexity of linear search?
Ans. O(n)
"""

def linear_search(arr, target):
    """
    Perform linear search on the given array to find the target element.
    
    Parameters:
    - arr: List of elements to search through.
    - target: Element to search for.

    Returns:
    - If the target is found, return the index of the target in the array.
    - If the target is not found, return -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


my_list = [4,2,7,1,9,5]
target_element = 7

result = linear_search(my_list, target_element)

if result != -1:
    print(f'Target element {target_element} found at index {result}.')
else:
    print(f'Target element {target_element} not found in the list.')
