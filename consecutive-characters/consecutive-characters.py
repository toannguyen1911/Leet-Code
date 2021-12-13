class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        max_val = -float('inf')
        for i in range(1, len(s)):
            #print(count)
            if s[i] == s[i-1]:
                count += 1
                continue
            elif count > max_val:
                    max_val = count
            count = 1
        return max_val if max_val > count else count
            