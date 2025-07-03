class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = "";
        n1 = len(word1);
        n2 = len(word2);
        i = 0;

        while (1):
            if (i >= n1):
                ans += word2[i:];
                break;
            if (i >= n2):
                ans += word1[i:];
                break;
            ans += word1[i] + word2[i];
            i += 1;
        return ans;