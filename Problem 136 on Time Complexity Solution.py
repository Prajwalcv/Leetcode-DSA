class Solution(object):
    def singleNumber(self, nums):
        if len(nums)==1:
            return nums[0]
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]=dic[i]+1
        for key,value in dic.items():
            if value==1:
                return key
