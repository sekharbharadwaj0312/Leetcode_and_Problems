def string_balance_test(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


s1 = input()
s2 = input()
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)
