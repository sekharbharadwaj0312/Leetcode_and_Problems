def isPalindrome(N):
    str1 = "" + str(N)
    len1 = len(str1)
    for i in range(int(len1 / 2)):
        if (str1[i] != str1[len1 - 1 - i]):
            return False
    return True
    
    
def PalinArray(arr ,n):
    for i in range(n):
        ans = isPalindrome(arr[i])
        if (ans == False):
            return False
    return True

