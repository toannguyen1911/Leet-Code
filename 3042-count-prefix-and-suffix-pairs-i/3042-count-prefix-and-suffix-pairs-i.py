class Solution:
    def isPrefixAndSuffix(self, s, word):
        if (word.startswith(s) and word.endswith(s)):
            return 1;
        return 0;

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0;
        for i in range (len(words)):
            for j in range(i +1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    ans += 1;
        
        return ans

        