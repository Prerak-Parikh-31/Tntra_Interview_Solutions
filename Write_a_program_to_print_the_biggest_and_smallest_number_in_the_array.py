'''Write a program to print the biggest and smallest number in the array.
Input: arr[] = {1, 2, 3, 4, 5}
Output: Maximum is: 5
Minimum is: 1

Input: arr[] = {5, 3, 7, 4, 2}
Output: Maximum is: 7
Minimum is: 2'''

def min_max(arr):
    minimum = arr[0]
    maximum = arr[0]
    if len(arr) == 1:
        maximum = arr[0]
        minimum = arr[0]
        print("Maximum is:", maximum)
        print("Minimum is:", minimum)
    else:
        if arr[0] > arr[1]:
            maximum = arr[0]
            minimum = arr[1]
        else:
            maximum = arr[1]
            minimum = arr[0]

        for i in range(2, len(arr)):
            if arr[i] > maximum:
                maximum = arr[i]
            elif arr[i] < minimum:
                minimum = arr[i]
        print("Maximum is:", maximum)
        print("Minimum is:", minimum)

# Input: arr = [1, 2, 3, 4, 5]
# Output: Maximum is: 5
# Minimum is: 1
arr1 = [1, 2, 3, 4, 5]
min_max(arr1)

# Input: arr = [5, 3, 7, 4, 2]
# Output: Maximum is: 7
# Minimum is: 2
arr2 = [5, 3, 7, 4, 2]
min_max(arr2)
