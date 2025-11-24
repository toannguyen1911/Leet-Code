class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        XOR Properties:
        - Same Numbers XOR to Zero
        - XOR with Zero Returns the Original Number
        - Commutative Property: giao hoán
        - Associative Property: kết hợp
        Ex: 0  [2 , 1 , 2 , 3 , 1]
        <=> 0 ^ 2 ^ 1 ^ 2 ^ 3 ^ 1
          = 0 ^ (2 ^ 2) ^ (1 ^ 1) ^ 3    ← Commutative & Associative
          = 0 ^ 0 ^ 0 ^ 3                ← Same numbers = 0
          = 3  
        

        Time complexity: O(n)
        Space complexity: O(1)
        """
        res = 0;

        for num in nums:
            res ^= num;

        return res;