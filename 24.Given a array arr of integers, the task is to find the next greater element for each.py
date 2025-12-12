class solution:
    def nextLargeElement(self,arr):
        n=len(arr)
        res=[-1]*n
        stack=[]
        
        #traverse from right to left
        for i in range(n-1,-1,-1):
            #pop smaller or equal element 
            while stack and stack [-1] <=arr[i]:
                stack.pop()
                
            if stack:
                res[i]=stack[-1]
            
            stack.append(arr[i])
        return res

arr=[1,3,2,4]
sol=solution()
print(sol.nextLargeElement(arr))
