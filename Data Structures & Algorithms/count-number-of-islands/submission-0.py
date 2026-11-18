class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir_x = [1, 0, -1, 0]
        dir_y = [0, 1, 0, -1]
        n = len(grid)
        m = len(grid[0])
        count = 0
        
        def bfs(i, j):
            q = deque()
            grid[i][j] = "0"
            q.append((i,j))
            while q:
                x, y = q.popleft()
                for dx, dy in zip(dir_x, dir_y):
                    new_x = x + dx
                    new_y = y + dy
                    
                    if new_x < 0 or new_y < 0 or new_x >= n or new_y >= m or grid[new_x][new_y] == "0":
                        continue
                    q.append((new_x, new_y))
                    grid[new_x][new_y] = "0"
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    bfs(i, j)
                    count+=1

        return count