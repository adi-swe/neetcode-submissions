class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        res = [intervals[0]]
        for j in range(len(intervals)):
            end = res[-1][1]
            if intervals[j][0] <= end:
                res[-1][1] = max(end, intervals[j][1])
            else:
                res.append(intervals[j])
        return  res