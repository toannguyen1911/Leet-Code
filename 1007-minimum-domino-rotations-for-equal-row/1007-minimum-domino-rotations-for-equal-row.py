class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        c_top = Counter(tops)
        c_bot = Counter(bottoms)

        n = len(tops)

        for k, v in c_top.items():
            if v + c_bot[k] >= n:
                # Check valid
                dup = 0
                for i in range(n):
                    if tops[i] != k and bottoms[i] != k:
                        break
                    elif tops[i] == bottoms[i]:
                        dup += 1
                else:
                    return min(v, c_bot[k]) - dup

        return -1