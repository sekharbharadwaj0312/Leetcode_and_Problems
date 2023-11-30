class Solution:
    def longest(self, names, n):
        str1 = ""
    	if (n == 0):
            return []
 
    # Initialize Max
        Max = len(names[0])
    
        # Create an array res
        res = []
    
        # Insert first element in res
        res.append(names[0])
    
        # Traverse the array
        for i in range(1,n):
    
            # If string with greater length
            # is found
            if (len(names[i]) > Max):
                Max = len(names[i])
                res.clear()
                res.append(names[i]);
    
            # If string with current max length
            elif(len(names[i]) == Max):
                res.append(names[i])
        
        for ele in res:
            str1 += ele
        
        return str1
 