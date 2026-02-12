from collections import Counter
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        responses=[set(arr) for arr in responses]
        responses_=[item for sub_list in responses for item in sub_list]
        counter=Counter(responses_)
        max_freq=counter[responses_[0]]
        desired_key=responses_[0]
        for key , val in counter.items():
            if val > max_freq:
                max_freq=val
                desired_key=key
            elif val == max_freq:
                max_freq=val
                desired_key=min(desired_key,key)
        return desired_key

        
        