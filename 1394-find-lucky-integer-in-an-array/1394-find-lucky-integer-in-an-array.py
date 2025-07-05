from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1;
        freq = Counter(arr);

        for num in freq.keys():
            count = freq[num];
            if count == num and count > ans:
                ans = count;
        return ans;
