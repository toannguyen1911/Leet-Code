class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = {5: 0, 10: 0, 20: 0}
        
        for bill in bills:
            cash[bill] += 1;
            
            if (bill == 5):
                continue;
  
            if (bill == 10):
                if (cash[5] < 0):
                    return False;
                cash[5] -= 1;
            if (bill == 20):
                if (cash[10] > 0 and cash[5] > 0):
                    cash[10] -=1;
                    cash[5] -= 1;
                    continue;
                if (cash[5] > 2):
                    cash[5] -= 3;
                    continue
                return False;
                
        return True;
        