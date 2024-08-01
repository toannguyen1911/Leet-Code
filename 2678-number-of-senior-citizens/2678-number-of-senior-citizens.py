class Solution:
    def countSeniors(self, details: List[str]) -> int:
        '''
        result = 0
        
        for detail in details:
            if (int(detail[11: 13]) > 60):
                result += 1;
               
        return result
        '''
        # code optimization
        return sum(1 if int(detail[11:13]) > 60 else 0 for detail in details)
    
        
        
        