class Solution:
    def numTeams(self, rating: List[int]) -> int:
        """
          Team constant 3 increase soldier or 3 decrease.
          Suppose the soldier in the middle has rating i
          Totol = Sum (left less i * right more i) + (left more i * right less i)
        """
        
        result = 0
        for i in range (1, len(rating) -1):
            r_less, r_more, l_less, l_more = 0, 0, 0, 0
            for j in range (len(rating)):
                if j == i:
                    continue
                if j < i:
                    if rating[i] < rating[j]:
                        l_less += 1
                    else:
                        l_more += 1
                else:
                    if rating[i] < rating[j]:
                        r_less += 1
                    else:
                        r_more += 1
            result +=  l_less *r_more + r_less *l_more
        
        return result
