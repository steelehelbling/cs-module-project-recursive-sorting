# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    # Your code here

    merged_arr = []
    left_index = 0
    right_index = 0

    while left_index < len(arrA) and right_index < len(arrB):

        if arrA[left_index] < arrB[right_index]:
            merged_arr.append(arrA[left_index])
            left_index = left_index + 1
        else:
            merged_arr.append(arrB[right_index])
            right_index = right_index + 1

    if left_index < len(arrA):
        merged_arr.extend(arrA[left_index:])

    if right_index < len(arrB):
        merged_arr.extend(arrB[right_index:])

    return merged_arr
print(merge([9,8,7,6,5,4,3,2,1], [15, 17, 16, 12, 17, 13, 14 ,12]))
# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1: 
        middle = len(arr) // 2 
        left = arr[:middle] 
        right = arr[middle:] 

        if len(left) > 1:
            left = merge_sort(left) 

        if len(right) > 1:
            right = merge_sort(right) 

        arr = merge(left, right) 


    return arr
    
print(merge_sort([9,8,7,6,5,4,3,2,1, 15, 17, 16, 12, 17, 13, 14 ,12]))
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

