class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        res = 0;
        n = len(nums);
        prefix = [0] *n;
        suffix = 0;

        for i in range(n -1):
            prefix[i +1] = prefix[i] + nums[i];

        for i in range(n -1, 0, -1):
            suffix += nums[i];
            if (prefix[i] - suffix) % 2 == 0:
                res += 1;
        
        return res;
