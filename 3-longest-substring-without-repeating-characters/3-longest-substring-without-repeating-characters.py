class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        total = 1
        if len(s) <= 1: return len(s)
        for i in range(len(s) -1):
            #length = 1
            for j in range(i +1, len(s)):
                if s[i: j].find(s[j]) == -1:
                    print()
                else:
                    if total < len(s[i: j]):
                        total = len(s[i: j])
                    print("s", s[i: j])
                    break
                if j == len(s) -1:
                    if total < len(s[i: j+1]):
                        total = len(s[i: j+1])
                    print("s", s[i: j+1])
            
        return total
                
            
            
        