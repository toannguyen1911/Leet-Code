from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = str(n)
        cnt = Counter(s)
        L = len(s)

        power = 1
        while len(str(power)) <= L:
            if Counter(str(power)) == cnt:
                return True
            power <<= 1  # nhân 2
        return False
