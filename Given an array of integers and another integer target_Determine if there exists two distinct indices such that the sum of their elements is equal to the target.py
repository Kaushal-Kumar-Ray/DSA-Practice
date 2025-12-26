class solution:
    def twoSum(self,arr,target):
        seen=set()
        
        for num in arr:
            needed=target-num
            if needed in seen:
                return True
            seen.add(num)
        return False
sol=solution()
print(sol.twoSum([0,-1,2,-3,1],-2))