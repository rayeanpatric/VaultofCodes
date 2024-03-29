# Merging Arrays
"""The bug in the merge sort code is in the merging step. 
The code fails to handle the case where the two subarrays have 
different lengths. If one subarray has more elements than the other, 
the code will continue to copy elements from the longer subarray to 
the main array even after the shorter subarray has been exhausted. 
This will result in the main array containing duplicate elements."""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Check if the longer subarray has any more elements.
    if i < len(left) or j < len(right):
        # Copy the remaining elements from the longer subarray to the main array.
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

arr = [38, 27, 43, 3, 9, 82, 10]
merged_arr = merge_sort(arr)
print(f"The sorted array is: {merged_arr}")
