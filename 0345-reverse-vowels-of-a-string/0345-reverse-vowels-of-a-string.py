class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [c for c in s if c in "aeiouAEIOU"];
        ans = [c if c not in "aeiouAEIOU" else vowels.pop() for c in s];

        return "".join(ans)