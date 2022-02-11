from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        for i in range(len(s2)):
            if i + k-1 == len(s2):
                return False
            #print(Counter(s1), Counter(s2[i :i +k]))
            #print(Counter(s1) == Counter(s2[i: i +k]))
            if Counter(s1) == Counter(s2[i: i +k]):
                return True