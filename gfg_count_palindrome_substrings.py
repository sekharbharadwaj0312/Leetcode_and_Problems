
class Solution:

    def CountPS(self, str, n):
        #User function Template for python3

        count = 0
        for i in range(N-1):
            for j in range(i+2,N+1):
                if S[i] == S[j-1]:
                    p = S[i:j]
                    if p ==p[::-1]:
                        count +=1
        return count        
