class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        store = [intervals[0]]
        for i in range(1,len(intervals)):
            start1, end1 = store[-1]
            start2, end2 = intervals[i]
            if start2 <= end1:
                store[-1] = [start1,max(end1,end2)]
            else:
                store.append([start2,end2])
        return store