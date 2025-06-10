from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        # find max a1 - a2
        # <=> max a1, min a2
        # a1: odd freq
        # a2: even freq
        freq = Counter(s);
        a1 = 0;
        a2 = 0;

        for num in freq.values():
            if num % 2 and num > a1:
                a1 = num;
            elif num % 2 == 0 and num > a2:
                a2 = num;
        return a1 - a2;