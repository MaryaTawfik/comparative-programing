from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        my_dict=defaultdict(list)
        mat=[]
        for i in strs:
            key="".join(sorted(i))
            my_dict[key].append(i)
        for val in my_dict.values():
            mat.append(val)
        return mat


        