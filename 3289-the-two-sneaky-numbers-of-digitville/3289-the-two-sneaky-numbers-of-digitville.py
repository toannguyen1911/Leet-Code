class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = [];
        nums.sort();
        n = len(nums);

        for i in range(n -1):
            if nums[i] == nums[i +1]:
                res.append(nums[i]);

        return res;