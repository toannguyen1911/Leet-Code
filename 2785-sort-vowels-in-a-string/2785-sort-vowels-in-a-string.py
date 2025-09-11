class Solution:
    def sortVowels(self, s: str) -> str:
        flag = 0;
        ans = list(s);
        vowels = [ch for ch in s if ch in "AEIOUaeiou"];
        vowels.sort();

        for i, ch in enumerate(ans):
            if ch in "AEIOUaeiou":
                ans[i] = vowels[flag];
                flag += 1;

        return "".join(ans);