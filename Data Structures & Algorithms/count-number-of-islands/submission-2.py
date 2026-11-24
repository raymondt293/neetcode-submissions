class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = 0

        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    q.append((i,j))
                    grid[i][j] = "0"
                    while q:
                        xi, yi = q.popleft()
                        for xy, dy in directions:
                            if (xi+xy) < 0 or (xi+xy) >= len(grid) or (yi+dy) < 0 or (yi+dy) >= len(grid[0]) or grid[xi+xy][yi+dy] == "0":
                                continue
                            nei = (xi+xy, yi+dy)
                            grid[xi+xy][yi+dy] = "0"
                            q.append(nei)
                    res += 1

        return res
                
                        



