class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        """
            Time complexity: O(n log n), due to sorting the array
            Space complexity: O(1)
        """
        res, prev = 0, -float('inf');
        nums.sort();

        # We can choose nums[i] -k or nums[i -1] +1
        for num in nums:
            choose = max(num -k, prev +1);
            # Check if our choice is still within allowed range
            if (choose <= num +k):
                res += 1;
                prev = choose;
        return res;