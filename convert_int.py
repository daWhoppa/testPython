def convert(n):
    # Write code here
    res = []
    n_str = str(n) 
    for c in n_str:
        res.append(int(c))
    return res

res = convert(10)
print(res)  # Output: [1, 0]