from collections import Counter;

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers);
        ans = 0;

        for key, num in freq.items():
            group_size = key + 1
            groups = ceil(num / group_size);
            ans += groups * group_size;
        return ans;
