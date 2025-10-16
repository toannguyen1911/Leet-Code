class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mex = float('inf');
        pos = 0;

        freq = defaultdict(int);
        for num in nums:
            freq[num % value] += 1;

        for i in range(value):
            if freq[i] == 0:
                return i;
            if freq[i] < mex:
                mex = freq[i];
                pos = i;
        return (value *mex) + pos;