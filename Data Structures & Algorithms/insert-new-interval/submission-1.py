class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        n = len(intervals)
        for i in range(n):
            end = res[-1][1]
            if end >= intervals[i][0]:
                res[-1][1] = max(end, intervals[i][1])
            else:
                res.append(intervals[i])

        return res