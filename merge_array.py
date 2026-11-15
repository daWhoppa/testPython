def rotate(arr):
    # Write code here
    result = []
    last = arr[-1]
    arr.pop((-1))
    result.extend([last])
    result.extend(arr)
    return list(result)

res = rotate([1, 2, 3, 4, 5])
print(res)  # Output: [5, 1, 2, 3, 4]