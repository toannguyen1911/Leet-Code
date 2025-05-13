class Solution:
    """
        t is number of transformations
        Rule:
            if c == 'z' => replace with 'ab'
            Otherwise => replace with next character
        return length of s
    """
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        ans = len(s);
        mod = 10**9 + 7;
        # convert to ascii
        # a = 97, z = 122
        for c in s:
            c = ord(c);
            ans += (c + t -1) // 122;
            ans %= mod;

        return ans;
        
