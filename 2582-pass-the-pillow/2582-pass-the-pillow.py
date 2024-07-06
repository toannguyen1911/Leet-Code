import math
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if (n - 1 >= time ):
            return time + 1;
        
        result = time % (n -1);
        l = math.ceil(time / (n -1) );
        
        if (result == 0):
            return 1 if (l % 2 == 0) else n
        
        return n - result if (l % 2 == 0) else result + 1;
        