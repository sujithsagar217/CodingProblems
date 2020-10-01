class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        lt=[]
        lt=lt+nums
        lt.sort()
        count=0
        res=[]
        for i in range(0,len(lt)):
            if(lt[i]!=nums[i]):
                res.append(i)
                count=count+1
        if(count==0):
            return count
        else:
            count=res[-1]-res[0]
            return count+1
