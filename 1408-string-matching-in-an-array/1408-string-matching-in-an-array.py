class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # sort string maybe is substring of another string
        words.sort(key=lambda s: len(s));
        ans = [];
        for i in range (len(words)):
            for j in range (i + 1, len(words)):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break;

        return ans;
        