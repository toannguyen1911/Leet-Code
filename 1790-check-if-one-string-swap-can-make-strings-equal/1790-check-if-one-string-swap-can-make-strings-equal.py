class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        ans = 0;
        root = 0;

        for i in range (len(s1)):
            if (s1[i] != s2[i]):
                ans += 1;
                if ans == 2:
                    swap = list(s2);
                    swap[i], swap[root] = swap[root], swap[i];
                    return s1 == ''.join(swap);
                root = i;

        return s1 == s2;