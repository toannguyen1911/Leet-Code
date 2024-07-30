class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = step = 0
        for c in s:
            if (c == 'b'):
                count += 1
                continue
            step = min(step + 1, count)
        
        return step