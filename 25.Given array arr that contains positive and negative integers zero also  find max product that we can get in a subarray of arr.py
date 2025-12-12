class solution:
    def maxProduct(self,arr):
        
        if not arr:
            return 0
        max_ending= min_ending = best = arr[0]
        
        for x in arr[1:]:
            #compute candidates before updating, beacause max_ending/ min_ending depends on the previous values:
            a=x
            b=x * max_ending
            c=x* min_ending
            
            max_ending= max(a,b,c)
            min_ending= min(a,b,c)
            
            if max_ending > best :
                best = max_ending
        return best
    