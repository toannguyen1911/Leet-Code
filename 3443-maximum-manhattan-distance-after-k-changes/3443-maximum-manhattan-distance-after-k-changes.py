class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x = y = 0;
        ans = 0;
        
        for i, c in enumerate(s):  
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'E':
                x += 1
            elif c == 'W':
                x -= 1

            real_dist = abs(x) + abs(y);
            dist = min(real_dist + 2 * k, i + 1);
            ans = max(ans, dist);
        
        return ans  ;