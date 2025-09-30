class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        """
            Action: 
            - if length n == 1, end
              else create newNums: length n -1
            - newNums[i] = nums[i] + nums[i +1] %10
            - Replace nums with newNums
        """
        n = len(nums);

        for i in range(n -1, 0, -1):
            new_nums = [];
            for j in range(i):
                new_nums.append((nums[j] + nums[j +1]) %10);
            nums = new_nums;

        return nums[0];