from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0;

        for num in nums:
            cnt = 0;
            s = 0;
            i = 1;

            while i * i <= num:
                if num % i == 0:
                    j = num // i;
                    cnt += 1;
                    s += i;
                    if i != j:
                        cnt += 1;
                        s += j;
                    if cnt > 4:
                        break;
                i += 1;
            if cnt == 4:
                res += s;

        return res;