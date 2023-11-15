class Solution:
    #Complete the below function
    def search(self,arr, N, X):
        
        if len(arr) != N:
            return -1
            
        for i in range(len(arr)):
            if arr[i] == X:
                return i
        return -1