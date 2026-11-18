def longestCommonPrefix(a):
    # Write code here
    smallest = min(a, key=len)

    scp = ""

    for i in range(len(smallest)):
        print(smallest)
        res = True
        for w in a:
            print(f"  {w}")
            if w.startswith(smallest) == False:
                res = False
            if res == True:
                scp = smallest
            else:
                smallest = smallest[:-1]
                break
        if res == True:
            break

    return scp

res = longestCommonPrefix(["flower", "flow", "flight", "flourish"])
print(res)  # Output: "fl"