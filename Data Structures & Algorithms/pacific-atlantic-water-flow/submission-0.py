class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(r, c, reachable):
            reachable.add((r,c))

            for dr, dc in directions:
                n_r, n_c = r + dr, c + dc
                if 0 <= n_r < rows and 0 <= n_c < cols:  
                    if (n_r, n_c) not in reachable and heights[n_r][n_c] >= heights[r][c]:
                        dfs(n_r, n_c, reachable)

    

        for r in range(rows):
            dfs(r, 0, pacific_reachable)
            dfs(r, cols-1, atlantic_reachable)
        for c in range(cols):
            dfs(0, c, pacific_reachable)
            dfs(rows-1, c, atlantic_reachable)
        
        return list(pacific_reachable & atlantic_reachable)