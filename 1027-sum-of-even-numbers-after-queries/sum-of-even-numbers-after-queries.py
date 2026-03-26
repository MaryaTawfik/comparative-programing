class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        even_sum = sum(x for x in nums if x % 2 == 0) 
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]

            ans.append(even_sum)

        return ans
        # for i in range (len(queries)):

        #     nums[queries[i][1]]+=queries [i][0]
        #     sum_=sum(list(filter(lambda a :a%2==0,nums)))
        #     ans.append(sum_)
        # return ans
        