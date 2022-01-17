class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        save = {}
        s = s.split()
        if len(pattern) != len(s): return False
        for i in range(len(pattern)):
            if save.get(pattern[i]) == None:
                for j in save:
                    if save.get(j) == s[i]:
                        return False
                save[pattern[i]] = s[i]
            else:
                if save.get(pattern[i]) != s[i]:
                    return False
        return True
        