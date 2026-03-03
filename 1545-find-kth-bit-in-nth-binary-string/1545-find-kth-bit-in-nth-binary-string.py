class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """
            S_i = S_i - 1 + "1" + reverse(invert(S_i - 1))
            len = 2 ^n -1
            mid = 2 ^(n -1)
            mirrored = len + 1 - k = 2 ^n - k

            Time complexity: O(n)
            Space complexity: O(n)
        """
        if n == 1:
            return "0";
        
        mid = 1 << (n - 1);   # 2^(n -1)
        
        if k == mid:
            return "1";
        
        if k < mid:
            return self.findKthBit(n - 1, k);
        
        # k > mid
        mirrored = (1 << n) - k; # 2^n -k
        bit = self.findKthBit(n - 1, mirrored);
        
        return "0" if bit == "1" else "1";