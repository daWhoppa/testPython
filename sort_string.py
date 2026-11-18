def sortString(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    dictLetterKey = dict(zip(letters, range(len(letters))))
    dicNumKey = dict(enumerate(letters))
    res = []
    res_1 = []

    for i in s:
        num = dictLetterKey[i]
        res_1.append(num)

    res_1.sort()

    for i in res_1:
        letter = dicNumKey[i]
        res.append(letter)

    return "".join(res)


res = sortString('hello')
print("".join(res))  # Output: 'ehllo'