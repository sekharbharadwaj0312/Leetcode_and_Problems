class Solution:
    def getSum(self, arr, n):
        sum = 0
        for i in range(n):
            sum += arr[i]
        return sum