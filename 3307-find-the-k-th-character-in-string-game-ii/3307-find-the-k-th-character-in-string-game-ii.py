class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        s = [];
        k -= 1;
        ans = 0;

        # Convert k to binary
        while k:
            s.append(k & 1);
            k >>= 1;
        
        for i in range(len(s)):
            if s[i] == 1:
                ans += operations[i];  

        return chr(ord('a') + ans % 26);
