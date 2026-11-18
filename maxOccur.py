def occurMax(a):
    # Write code here
    count_dict = {}
    for num in a:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    print(count_dict)
    sorted_items = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    print(sorted_items)
    return sorted_items[0][0]

res = occurMax([5, 5, 1, 2, 2, 3, 3, 3, 4])
print(res)  # Output: 3


