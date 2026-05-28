class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        sum_=0
        left=0
        arr=[-1 for i in range(len(nums))]
        if len(nums)<(2*k)+1:
            return arr
        if k==0:
            return nums
        sum_=sum(nums[:(2*k)+1])
        # print(sum_)
        arr[k]=sum_//(2*k+1)
        for right in range((2*k)+1,len(nums)):
            if right - left >= (2*k)+1:
                sum_+=nums[right]
                sum_-=nums[left]
                left+=1
                arr[(left+right)//2]=sum_//(2*k+1)
        return arr
