class Solution:
    def isPalindrome(self, s: str) -> bool:
        f_index = 0;
        l_index = len(s) - 1;
        
        while (f_index < l_index):
            if (not s[f_index].isalpha() and not s[f_index].isnumeric()):
                f_index += 1;
                continue;
            if (not s[l_index].isalpha() and not s[l_index].isnumeric()):
                l_index -= 1;
                continue;
            if (s[f_index].lower() != s[l_index].lower()):
                return False;
            f_index += 1;
            l_index -= 1;
        return True;
        