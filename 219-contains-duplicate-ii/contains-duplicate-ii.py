class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict=defaultdict(list)
        for i in range(len(nums)):
            my_dict[nums[i]].append(i)

        for i in my_dict.values():
            if len(i)<=1:
                continue
            i.sort()
            for j in range(len(i)):
                for m in range(j+1,len(i)):
                    if abs(i[j]-i[m]) <= k:
                        return True
        return False

        

        