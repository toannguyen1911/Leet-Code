class Solution:
    def findKthNumber(self, n, k):
        current_prefix = 1;
        k -= 1  # Decrement k to handle zero-based indexing
        
        while k > 0:
            print(k);
            count = self.countNumbersWithPrefix(current_prefix, n);
            print(count)
            # Move to the next prefix
            if k >= count:
                current_prefix += 1;  
                k -= count;
                continue;
            # Go deeper in the current prefix
            current_prefix *= 10;  
            k -= 1;
        
        return current_prefix;

    def countNumbersWithPrefix(self, prefix, n):
        first_number = prefix;
        next_number = prefix + 1;
        total_count = 0;

        while first_number <= n:
            total_count += min(n + 1, next_number) - first_number;
            first_number *= 10;
            next_number *= 10;

        return total_count;