class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
            Time complexity: O(n)
            Space complexity: O(2 ^k)
        """
        n = len(s);
        if n < k:
            return False;
        
        seen = set();
        
        # Find all possible substrings of length k within the original string.
        for i in range(n - k + 1):
            seen.add(s[i :i+k]);
        
        # For a binary string of length k, there are exactly 2^k possible binary codes.
        return len(seen) == (1 << k);