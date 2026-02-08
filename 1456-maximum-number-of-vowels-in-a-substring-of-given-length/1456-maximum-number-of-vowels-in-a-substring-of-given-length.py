class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = list('aeiou');
        n = len(s);
        window = 0;

        for i in range(k):
            if s[i] in vowel:
                window += 1;
        
        res = window;
        
        for i in range(k, n):
            if res == k:
                return res;
            if s[i] in vowel:
                window += 1;
            if s[i - k] in vowel:
                window -= 1;
            res = max(res, window);

        return res;