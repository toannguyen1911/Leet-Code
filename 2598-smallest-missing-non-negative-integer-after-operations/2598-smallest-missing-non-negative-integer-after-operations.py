class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq = defaultdict(int);
        for num in nums:
            freq[num % value] += 1;

        min_freq = float('inf');
        remainder = 0;
        for i in range(value):
            if freq[i] == 0:
                # If this remainder never appears,
                # the smallest missing number is exactly i
                return i;

            # Find the remainder that appears least often.
            if freq[i] < min_freq:
                min_freq = freq[i];
                remainder = i;
        return (value * min_freq) + remainder;