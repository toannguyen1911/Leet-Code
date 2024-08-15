class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = {5: 0, 10: 0, 20: 0}
        
        for bill in bills:
            cash[bill] += 1;
            
            if (bill == 5):
                continue;
  
            if (cash[5] < 1):
                return False;
            
            cash[5] -= 1;
            if (bill == 10):
                continue;
            if (cash[10] < 1):
                if (cash[5] < 2):
                    return False;
                cash[5] -= 2;
                continue;
            cash[10] -= 1;
                    
        return True;
        