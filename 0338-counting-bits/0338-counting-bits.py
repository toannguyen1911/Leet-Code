class Solution:    
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
        
        