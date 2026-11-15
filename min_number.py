def findMin(arr):
    # Write code here
    min_num = arr[0]
    for n in arr:
        if n < min_num:
            min_num = n
    return min_num

res = findMin([3, 1, 4, 1, 5, 9])
print(res)  # Output: 1