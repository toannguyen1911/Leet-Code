class Solution:
    """
        Brute Force with Sets
    """
    def countPalindromicSubsequence(self, s: str) -> int:
        # Answer format = xyx
        # set x, find another y

        l = 0;
        r = len(s) -1;
        ans = 0;
        memory = [];

        while (l < r):
            # just check the unique x
            if (s[l] in memory):
                l += 1;
                continue;
            # find x but y not existed, ignore and continue
            if (s[l] == s[r] and l +1 >= r):
                l += 1;
                r = len(s) - 1;
                continue;
            elif (s[l] == s[r]):
                # next, we need to find the unique y
                # get all unique y
                y = list(set(s[l +1: r]));
                ans += len(y);
                memory.append(s[l]);
                l += 1;
                r = len(s) -1;
                continue;
            
            r -= 1;
            if (l >= r and l < len(s) -3):
                memory.append(s[l]);
                l += 1;
                r = len(s) -1;
        return ans;
            
