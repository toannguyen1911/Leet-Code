class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans = [];
        zero_count = 0;
        for i in range (len(nums) -1):
            if (nums[i] == 0):
                zero_count += 1;
                continue;
            if (nums[i] == nums[i + 1]):
                nums[i] *= 2;
                nums[i + 1] = 0;
            
            ans.append(nums[i]);
        
        return ans + [nums[-1]] + [0] * zero_count if nums[-1] != 0 else ans + [0] * (zero_count + 1);