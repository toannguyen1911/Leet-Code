class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        """
        Step 1: Multi-source BFS
        Compute dist[r][c] = shortest distance to any thief

        Step 2: Max-heap Dijkstra
        Maximize the minimum dist along the path

        Time Complexity: O(n * m * log(n * m))
        Space Complexity: O(n * m)
        """

        n, m = len(grid), len(grid[0]);
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)];

        # Find all thiefs O(m * n)
        dist = [[float('inf')] * m for _ in range(n)];
        thiefs = deque();

        for i in range (n):
            for j in range(m):
                if grid[i][j] == 1:
                    thiefs.append((i, j));
                    dist[i][j] = 0;

        # Calculate the minimum distance from the thieves to each cell
        # BFS O(4 * m * n)
        while thiefs:
            x, y = thiefs.popleft();

            for dx, dy in directions:
                nx, ny = x + dx, y + dy;
                
                if (0 <= nx < n and  0 <= ny < m and dist[x][y] + 1 < dist[nx][ny]):
                    dist[nx][ny] = dist[x][y] + 1;
                    thiefs.append((nx, ny));

        # Find the path with the maximum safeness factor
        # So use Max Heap (safe, row, col), every push/pop operation costs O(log(n*m)
        # and modified Dijkstra O(n * m * log(n * m))
        visited = [[False] * m for _ in range(n)];

        # Python only has min heap, so store negative cost to simulate max heap
        heap = [(-dist[0][0], 0, 0)];

        while heap:
            neg_safe, x, y = heapq.heappop(heap);
            safe = -neg_safe;

            if x == n -1 and y == m -1:
                return safe;

            if visited[x][y]:
                continue;

            visited[x][y] = True;

            for dx, dy in directions:
                nx, ny = x + dx, y + dy;

                if (0 <= nx < n and  0 <= ny < m and not visited[nx][ny]):
                    new_safe = min(safe, dist[nx][ny]);
                    heapq.heappush(heap, (-new_safe, nx, ny));
        
        return -1;