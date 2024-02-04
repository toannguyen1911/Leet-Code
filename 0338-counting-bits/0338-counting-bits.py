class Solution:
    def toBinary(self, x: int): 
        if (x <= 1): 
            return x % 2;
        return self.toBinary(x // 2) + x % 2;
                   
    def countBits(self, n: int) -> List[int]:
        result = [];
        memory = {};
        
        for index in range(n + 1):
            count = 0;
            x = index;
            
            while (x > 0):
                if (x in memory):
                    count += memory[x];
                    break;
                count += x % 2;
                x = x //2;
                
            if (index not in memory):
                memory[index] = count;
            result.append(count);
        
        return result;
        
        