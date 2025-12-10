class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10 **9 + 7;

        def permutation(n):
            fact = n;
            for i in range(2, n):
                fact = (fact *i) % MOD;
            return fact;
        
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        res = 0;
        n = len(complexity);
        root = complexity[0];

        for i in range(1, n):
            c = complexity[i];
            if c <= root:
                return res;

        res = permutation(n -1);
        return res;
