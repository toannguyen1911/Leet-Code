class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """        
        res = 0;

        res = (high - low +1) //2;

        if (low % 2 and high % 2):
            res += 1;
        return res;