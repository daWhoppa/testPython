def isPalindrome(num):
    # Write code here
    str_num = str(num)
    reversed_str = ""
    for c in str_num:
        reversed_str = c + reversed_str
    return str_num == reversed_str



str = "12345"
reversed_str = ""
for c in str:
    print(c)
    reversed_str = reversed_str + c
print("============")
print(reversed_str)