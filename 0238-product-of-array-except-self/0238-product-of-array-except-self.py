class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums);
        ans = [0] *n;
        prefix = [1] *n;
        suffix = [1] *n;
        
        flag = 1;
        for i in range(1, n):
            flag *= nums[i -1];
            prefix[i] = flag;
        
        flag = 1;
        ans[-1] = prefix[-1];
        for j in range(n -2, -1, -1):
            flag *= nums[j +1];
            ans[j] = prefix[j] * flag;
            suffix[j] = flag;
            
        return ans;
