class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        def dfs(index, total, path):
            if index >= len(nums) or total > target:
                return
            if total == target: 
                res.append(list(path))
                return
            path.append(nums[index])
            dfs(index, total + nums[index] , path)
            path.pop()
            dfs(index+1, total, path)

        res = []
        dfs(index=0, total=0, path=[])
        return res