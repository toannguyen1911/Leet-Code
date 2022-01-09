class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        a = x.copy()
        a.reverse()
        print(x, a)
        return x == a
        