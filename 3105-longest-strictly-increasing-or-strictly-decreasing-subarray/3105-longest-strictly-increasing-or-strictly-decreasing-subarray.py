class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1;
        count = 1;
        n = len(nums);

        for i in range (n -1):
            # update ans
            if (count > ans):
                ans = count;
            # fast stop
            if (ans >= n - i):
                return ans;
            
            # reset loop variable
            op = None;
            root = nums[i];
            count = 1;
            for j in range (i +1, len(nums)):
                if root == nums[j]:
                    break;
                # update operator
                if (op == None):
                    op = 1 if root > nums[j] else -1;
                    root = nums[j]
                    count += 1;
                    continue;
                compare = (root - nums[j]) * op;
                if (compare <= 0):
                    break;
                # update  sub array
                count += 1;
                root = nums[j];
               
        return count;