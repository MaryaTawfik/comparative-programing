class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zmax = max(heights)
        counter = [[] for _ in range(zmax+1)]
        for name, h in zip(names, heights):
            counter[h].append(name)
        
        ans = []
        for h in range(zmax, -1, -1):
            for name in counter[h]:
                ans.append(name)
        
        return ans