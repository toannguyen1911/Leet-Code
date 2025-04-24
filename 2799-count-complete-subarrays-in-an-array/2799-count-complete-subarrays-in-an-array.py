from collections import Counter
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0;
        parent = Counter(nums)
        distinct_parent = len(parent);
        

        for i in range(0, len(nums) - distinct_parent +1):
            temp_arr = set()
            for j in range(i, len(nums)):
                temp_arr.add(nums[j]);
                if len(temp_arr) == distinct_parent:
                    ans += 1
        return ans;
