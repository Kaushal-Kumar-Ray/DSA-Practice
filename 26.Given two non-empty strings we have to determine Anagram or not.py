class solution:
    def areAnagrams(self,s1,s2):
        if len(s1)!=len(s2):
            return False
        freq =[0]*26
        
        for ch in s1:
            freq[ord(ch)-ord('a')] +=1
            
        for ch in s2:
            freq[ord(ch)-ord('a')] -=1
        
        return all(count==0 for count in freq)

s1=input().strip()
s2=input().strip()

obj=solution()
print(obj.areAnagrams(s1,s2))