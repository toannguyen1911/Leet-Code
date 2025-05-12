class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = [];
        freq = Counter(digits);

        # Num <=> xyz
        for num in range(100, 1000, 2):
            x, y, z = num % 10, (num //10) %10, num // 100;
            freq[x] -= 1;
            freq[y] -= 1;
            freq[z] -= 1;

            if (freq[x] >= 0 and freq[y] >= 0 and freq[z] >= 0):
                ans.append(num);
            freq[x] += 1;
            freq[y] += 1;
            freq[z] += 1;
        
        return ans;