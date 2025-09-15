class Solution:
    def reverseWords(self, s: str) -> str:
        ans = [];
        words = s.split(" ")[::-1];

        for word in words:
            if word == '':
                continue;
            ans.append(word);

        return " ".join(ans);