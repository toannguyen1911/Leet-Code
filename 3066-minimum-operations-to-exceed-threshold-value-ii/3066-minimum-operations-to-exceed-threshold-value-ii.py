class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort();
        b = [];
        i = j = ans = 0;

        def findSmallestNumber(i, j):
            if i < len(nums) and (j >= len(b) or nums[i] <= b[j]):
                x = nums[i];
                i += 1;
            else:
                x = b[j];
                j += 1;
            return [x, i, j];

        while True:
            # Get smallest number from 2 arrays
            x, i, j = findSmallestNumber(i, j);
            if x >= k:
                return ans;
            
            # Get 2st smallest number from 2 arrays
            y, i, j = findSmallestNumber(i, j);
            
            # Add value of operation
            b.append(x *2 + y);
            ans += 1;

        return ans;