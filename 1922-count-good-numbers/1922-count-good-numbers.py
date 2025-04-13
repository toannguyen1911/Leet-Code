class Solution:
    module = 10 **9 + 7;

    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5;
        # number of prime: 2, 3, 5, 7 -> 4
        # number of even: 0, 2, 4, 6, 8 -> 5
        # Total good number: 5^ (even_position) * 4 ^ (odd_position)
        odd_positions = n //2;
        even_positions  = n - odd_positions;
        even_ways = self.binary_exponentiation(5, even_positions);
        odd_ways = self.binary_exponentiation(4, odd_positions);

        return int (even_ways * odd_ways % self.module);  
    
    """
        Use this function will reduces the time from O(n) to O(log n).
    """
    def binary_exponentiation(self, base, power):
        result = 1;
        base %= self.module;

        while power > 0:
            # x & 1 is equivalent to x % 2.
            if power & 1: 
                result = (result * base) % self.module;
            base = (base * base) % self.module;
            # x >> 1 is equivalent to x // 2
            power //= 2;

        return result;