from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = 0;
        memory = defaultdict(int);

        # Calculate the number of pairs with the same product.
        for i in range (len(nums) -1):
            for j in range(i +1, len(nums)):
                prod = nums[i] * nums[j];
                ans += 8 * memory[prod];
                memory[prod] += 1;

        return ans;