class Solution:
    # def find(self, nums: List[int], n: int, left: int, right: int)
    def rangeSum(self, nums: List[int], n: int, left: int, right: int):
        sub_sum = nums.copy()
        for i in range (n -1):
            sum_val = nums[i]
            for j in range(i + 1, n):
                sum_val += nums[j]
                sub_sum.append(sum_val)
        sub_sum.sort()
        mod = 10**9 + 7
        return sum(sub_sum[left -1: right]) % mod
        