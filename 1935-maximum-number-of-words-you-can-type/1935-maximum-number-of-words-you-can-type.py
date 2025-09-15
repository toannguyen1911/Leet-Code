class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0;

        for word in text.split(" "):
            is_valid = True;
            for c in brokenLetters:
                if c in word:
                    is_valid = False;
                    break;
            if (is_valid):
                ans += 1;

        return ans;