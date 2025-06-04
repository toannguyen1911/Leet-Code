class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word;
        
        ans = "";
        n = len(word);
        max_len = n - numFriends + 1;
  
        for i in range(n):
            last = min(i + max_len, n);
            sub = word[i: last];

            if sub > ans:
                ans = sub;
        return ans;