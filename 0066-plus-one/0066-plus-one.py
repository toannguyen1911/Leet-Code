class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:        
        for index in range(len(digits), 0, -1):
            if (digits[index -1] < 9):
                digits[index -1] += 1;
                return digits; 
            digits[index -1] = 0;
            
        return [1] + digits;