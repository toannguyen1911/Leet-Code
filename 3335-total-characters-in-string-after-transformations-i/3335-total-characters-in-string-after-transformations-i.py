class Solution:
    """
        t is number of transformations
        Rule:
            if c == 'z' => replace with 'ab'
            Otherwise => replace with next character
        return length of s
    """
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        def bruteForce(s, t):
            dp = [0] * 26;
            ans = 0;
            mod = 10**9 + 7;

            for c in s:
                dp[ord(c) -97] += 1;
            
            for i in range(t):
                cur = [0] * 26;

                # check z
                if dp[25]:
                    cur[0] = (cur[0] + dp[25]) % mod;
                    cur[1] = (cur[1] + dp[25]) % mod;
                for j in range(25):
                    num = dp[j]
                    if (num):
                        cur[j +1] = (cur[j + 1] + num) % mod;
                dp = cur
            for m in dp:
                ans = (ans + m) % mod;
            return ans;

        def dynamicProgram(s, t):
            ans = 0;
            mod = 10**9 + 7;
            dp = [0] * (t + 26);

            # Start with 'a'
            # dp[i]: 
            #   i < 26: dp[i] = 1; <=> next character
            #   i >= 26: dp[i] = dp[i -26] + dp[i -25] <=> a, b
            
            for i in range(26): 
                dp[i] = 1;
            for i in range(26, t + 26):
                dp[i] = (dp[i - 26] + dp[i - 25]) % mod;
            
            for ch in s:
                dp_result = dp[ord(ch) - ord('a') + t];
                ans = (ans + dp_result) % mod;
            
            return ans;
        
        # return bruteForce(s, t);
        return dynamicProgram(s, t);
        
