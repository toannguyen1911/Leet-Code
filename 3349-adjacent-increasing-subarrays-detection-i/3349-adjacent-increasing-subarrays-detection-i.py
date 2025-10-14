class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def isStrictlyIncreasing(a):
            num = nums[a];
            print('check', a)

            for i in range(a +1, a +k):
                print('i', i)
                # not valid, let move to next circle
                if nums[i] <= nums[i -1]: 
                    return i;
            return False;

        res = False;
        a = 0;
        n = len(nums);

        while (a <= n - (2 *k)):
            print('a', a)
            valid = isStrictlyIncreasing(a);
            
            print('l', valid)
            if valid:
                a = valid;
                continue;

            # first right
            right_valid = isStrictlyIncreasing(a + k);
            print('r', right_valid)
            if (right_valid == False):
                return True;
            a += 1;

        return res;