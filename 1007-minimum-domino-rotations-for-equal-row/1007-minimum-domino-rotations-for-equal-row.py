class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops);
        counter = [0] * 6;

        # Target: All the values in tops are the same, or all the values in bottoms are the same.
        # Suppose tops or bottoms contain all "target" values.
        for i in range (n):
            counter[tops[i] -1] += 1;
            if bottoms[i] != tops[i]:
                counter[bottoms[i] -1] += 1;

        # Target can only be the first value of tops or bottoms.
        if counter[tops[0] -1] < n and counter[bottoms[0] -1] < n:
            return -1;
        
        target = tops[0] if counter[tops[0] -1] == n else bottoms[0];
        t_target = 0;
        b_target = 0;
        
        for i in range(n):
            if tops[i] == bottoms[i]:
                continue;
            if tops[i] == target:
                t_target += 1;
            if bottoms[i] == target:
                b_target += 1;

        return min(t_target, b_target);
       
