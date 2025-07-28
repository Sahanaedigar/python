# Binary Search Algorithm (Iterative)
# -----------------------------------
# Binary search is an efficient algorithm to find the position of a target element in a **sorted array**.
# Time Complexity: O(log n)
# It works by repeatedly dividing the search interval in half.

def binarySearch(arr, target):
    # Step 1: Set initial left and right pointers
    left = 0
    right = len(arr) - 1

    # Step 2: Loop until the search space is valid
    while left <= right:
        # Step 3: Calculate the middle index
        middle = (left + right) // 2

        # Step 4: Compare the middle element with the target
        if arr[middle] == target:
            return middle, arr[middle]  # Target found, return index and value
        elif target > arr[middle]:
            # Step 5a: If target is greater, ignore left half
            left = middle + 1
        else:
            # Step 5b: If target is smaller, ignore right half
            right = middle - 1

    # Step 6: Target not found
    return -1

# Example usage
# The array must be sorted in ascending order
arr = [2, 5, 10, 15, 20, 25, 30]
target = 20

# Output will be the index and value if found, else -1
print(binarySearch(arr, target))
