class Solution:
    def toBinary(self, x: int): 
        if (x <= 1): 
            return x % 2;
        return self.toBinary(x // 2) + x % 2;
                   
    def countBits(self, n: int) -> List[int]:
        result = [];
        for index in range(n + 1):
            result.append(self.toBinary(index));
        return result;
        
        