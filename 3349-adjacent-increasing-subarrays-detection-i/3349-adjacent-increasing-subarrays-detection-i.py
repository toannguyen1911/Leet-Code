class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

        def firstNonIncreasing(start):
            """
                Returns the first index inside the subarray [start, start + k)
                where the strictly increasing condition fails.
                Returns None if the subarray is strictly increasing.
            """

            for i in range(start +1, start +k):
                if nums[i] <= nums[i -1]: 
                    return i;
            return None;

        a = 0;
        n = len(nums);

        while (a <= n - (2 *k)):
            left_break = firstNonIncreasing(a);
            if left_break:
                a = left_break;
                continue;

            right_break  = firstNonIncreasing(a + k);
            if (right_break is None):
                # both left and right subarrays are strictly increasing
                return True;
            a += 1;

        return False;