class Solution:
    def sumOfMatrix(self,N,M,Grid):
        sum1 = 0
        for i in Grid:
            sum1 += sum(i)
        return sum1