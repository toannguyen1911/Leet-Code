class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s);
        ans = 0;
        total = 0; # Value of substring
        flag = True; # To mark substring is valid number

        for i in range (n -1, -1, -1):
            if (s[i] == '0'):
                ans += 1;
                continue;
            if (flag):
                total += 2 ** (n - i - 1);
                if (total <= k):
                    ans += 1;
                    continue;
                flag = False;
        return ans;