class solution:
    def maxlength(self,arr):
        prefix_sum=0
        max_length=0
        seen={}
        
        for i in range (len(arr)):
            prefix_sum += arr[i]
            
            if prefix_sum==0:
                max_length=i+1
            
            elif prefix_sum in seen:
                max_length=max(max_length,i-seen[prefix_sum])
            else:
                seen[prefix_sum]=i
        return max_length

arr=list(map(int,input().strip().split()))
print(solution().maxlength(arr))