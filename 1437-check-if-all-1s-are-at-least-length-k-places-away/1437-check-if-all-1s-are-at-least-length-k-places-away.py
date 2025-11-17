class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums);
        pos = -1;

        for i in range(n):
            if nums[i] == 1:
                if pos != -1 and i - pos <= k:
                    return False;
                pos = i;

        return True;