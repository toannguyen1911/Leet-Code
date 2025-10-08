class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums);
        ans = [1] *n;
        suffix = 1;
        
        # Calculate the prefix
        for i in range(1, n):
            ans[i] = ans[i -1] * nums[i -1];
            
        for j in range(n -1, -1, -1):
            ans[j] *= suffix;
            suffix *= nums[j];

        return ans;
