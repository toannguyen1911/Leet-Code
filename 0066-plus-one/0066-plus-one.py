class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = 0;
        
        if (len(digits) == 1):
            if (digits[0] == 9):
                return [1, 0];
            return [digits[0] +1];
        
        for index in range(len(digits), 0, -1):
            if (digits[index -1] < 9):
                temp = 0; 
                digits[index -1] += 1;
                break;
            
            if (digits[index -1] == 9):
                digits[index -1] = 0;
                temp = 1;
            
        if (temp > 0):
            digits[0] = 0;
            return [1] + digits;
        return digits