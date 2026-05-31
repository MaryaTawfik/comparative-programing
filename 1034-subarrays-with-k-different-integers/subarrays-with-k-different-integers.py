from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        visited=set()
        def atmost(k):
            left=0
            count=0
            freq=defaultdict(int)

            for right in range(len(nums)):
                freq[nums[right]]+=1
                # if len(freq)<=k:
                #     count+=right-left+1
                # else:
                while len(freq)>k:
                    freq[nums[left]]-=1
                    if freq[nums[left]]==0:
                        freq.pop(nums[left])
                    left+=1
                count+=right-left+1
            return count
        ans=atmost(k)-atmost(k-1)
        return ans