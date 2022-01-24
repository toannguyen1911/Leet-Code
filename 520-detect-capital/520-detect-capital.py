class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if word.isupper() or word.islower() or word[1:].islower():
            return True
        return False