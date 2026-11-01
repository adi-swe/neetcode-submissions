class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 1 2 6
        # 24 12 4 1

        # 1 -1 -1 0 0
        # 0 0 -9 3 1 
        n = len(nums)
        # left = [1] * n
        # right = [1] * n
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            # left[i] = left[i-1] * nums[i-1]

        # print(left)
        print(prefix)
        postfix = 1
        for i in range(n-1, -1, -1):
            # right[i] = right[i+1] * nums[i+1]
            res[i] *= postfix
            postfix *= nums[i]
        print(postfix)
        # for i in range(n):
        #     res[i] = left[i] * right[i]
        return res