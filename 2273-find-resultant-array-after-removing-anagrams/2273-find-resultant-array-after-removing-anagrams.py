class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]];
        n = len(words);
        freq = [Counter(w) for w in words]

        for i in range(1, n):
            if freq[i] != freq[i -1]:
                res.append(words[i]);
                
        return res;