class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        midpoint = len(nums) // 2;
        
        return sorted(nums)[midpoint]