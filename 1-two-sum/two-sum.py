# from collections import defualtdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        traker = defaultdict(list)
        left , right = 0 , len(nums)-1

        ans=[]

        for i in range(len(nums)):
            traker[nums[i]].append(i) 
        print(traker)
        nums.sort()
        while left < right:

            if nums[left] + nums[right] == target:
                # return [traker[nums[left]] , traker[nums[right]]]
                ans.append(traker[nums[left]][-1])
                traker[nums[left]].pop()
                ans.append(traker[nums[right]][-1])
                traker[nums[right]].pop()
                return ans
                
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1



        
















        # k=[]
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i]+nums[j]==target and i!=j:
        #           k.append(i)
        #           k.append(j)
        # return list(set(k)) 
        