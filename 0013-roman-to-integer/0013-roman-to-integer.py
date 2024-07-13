class Solution:
    def romanToInt(self, s: str) -> int:
        number = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
        cur_v, pre_v = 0, number[s[0]];
        sum_val = 0;
        
        for i in range (1, len(s)):
            cur_v = number[s[i]];
            flag = cur_v - pre_v;
            if (flag > 0 and (flag % 4 == 0 or flag % 9 == 0)):
                pre_v = 0;
                sum_val += flag;
                continue;
            sum_val += pre_v;
            pre_v = cur_v
        return sum_val + pre_v;