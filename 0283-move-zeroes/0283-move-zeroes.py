class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mark = 0;
        i, n = 0, len(nums);

        while (i < n):
            if nums[i] != 0:
                nums[i], nums[mark] = nums[mark], nums[i];
                mark += 1;
            i += 1;
        