class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        state, countT = {}, {}
        start = 0
        
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('inf')
        for end in range(len(s)):
            c = s[end]
            state[c] = state.get(c,0)+1

            if c in countT and state[c] == countT[c]:
                have += 1
            
            while have == need:
                if (end - start + 1) < resLen:
                    res = [start, end]
                    # print(res)
                    resLen = end - start + 1

                state[s[start]] -= 1
                if s[start] in countT and state[s[start]] < countT[s[start]]:
                    have -= 1
                start += 1

        start, end = res
        return s[start:end+1] if resLen != float('inf') else ""