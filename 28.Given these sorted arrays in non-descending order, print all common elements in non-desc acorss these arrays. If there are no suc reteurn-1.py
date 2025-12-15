class solution:
    def commomElements(self, arr1, arr2, arr3):
        i=j=k=0
        result=[]
        
        while i<len(arr1) and j<len(arr2) and k <len(arr3):
            if arr1[i] ==arr2[j] == arr3[k]:
                result.append(arr1[i])
                val=arr1[i]
                
                while i< len(arr1) and arr1[i] == val:
                    i+=1
                while j<len(arr2) and arr2[j] == val:
                    j+=1
                while k<len(arr3) and arr3[k] == val:
                    k+=1
            elif arr1[i] <  arr3[j]:
                i+=1
            elif arr2[j] < arr3[k]:
                j+=1
            else:
                k+=1 
        return result if result else[-1]

arr1=list(map(int,input().split()))            
arr2=list(map(int,input().split()))            
arr3=list(map(int,input().split()))            
sol=solution()
print(sol.commomElements(arr1,arr2,arr3))
