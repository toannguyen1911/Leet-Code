class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0;
        for num in range(low, high + 1):
            s = str(num);
            if (len(s) % 2): 
                continue;
            half  = len(s) // 2;
            ans += 1 if sum(int(s[i]) for i in range(half)) == sum(int(s[i]) for i in range(half, len(s))) else 0;
        return ans;