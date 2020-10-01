class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        lt=[]
        i=0
        st=list(set(arr))
        for i in range(0,len(st)):
            lt.append(arr.count(st[i]))
        if(len(st)==len(set(lt))):
            return True
        else:
            return False
            
            
            
        
