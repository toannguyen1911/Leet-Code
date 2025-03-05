class Solution:
    def coloredCells(self, n: int) -> int:
        #  1 5 13 
        # n = 4, ans = 25
        # match:
        # n = 1: 2n -1 
        """
            n = 1: 2n -1
            n = 2: 2n -1 + 2(2n -3)
            n = 3: (2n -1) + 2(2n -3) + 3(2n - 5)
            => ans = 4n^2 - 2n - 2*(1 + 3 + 5 + ... + 2n -1)
        """
        i = 1;
        ans = 4 * n *n - 2 * n;

        while (i <= n):
            ans -= 2*(2*i - 1);      
            i += 1;
        
        return ans + 1;