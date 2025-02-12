class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_map = defaultdict(lambda: [0, 0])
        for num in nums:
            digit_sum = self.digSum(num)
            first_max, second_max = digit_sum_map[digit_sum]
            if num > first_max:
                second_max = first_max
                first_max = num
            elif num > second_max:
                second_max = num
            digit_sum_map[digit_sum] = [first_max, second_max]

        max_sum = -1
        for first_max, second_max in digit_sum_map.values():
            if second_max > 0:
                max_sum = max(max_sum, first_max + second_max)
        return max_sum

    def digSum(self, x: int) -> int:
        return sum(int(digit) for digit in str(x))