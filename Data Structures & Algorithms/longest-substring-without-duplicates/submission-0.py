class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        state = {}
        count = 0
        l = 0
        for r in range(len(s)):
            if s[r] in state:
                l = max(state[s[r]]+1, l)
            state[s[r]] = r
            count = max(count, r-l+1)
        return count
