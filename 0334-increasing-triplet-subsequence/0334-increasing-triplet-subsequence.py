class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        res = False;
        first = second = float('inf');

        for num in nums:
            if num > first and num > second:
                return True;
            if num <= first:
                first = num;
            elif num < second:
                second = num;
        return res;