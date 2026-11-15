def lens(arr):
    # Write code here:
    lengths = []
    for s in arr:
        lengths.append(len(s))
    return lengths

res = lens(["hello", "world", "Python"])
print(res)  # Output: [5, 5, 6]