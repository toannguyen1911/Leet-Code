class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s);
        new_s = '';

        while(n > 2):
            new_s = '';
            for i in range(n -1):
                c = (int(s[i]) + int(s[i + 1])) % 10;
                new_s += str(c);  
            s = new_s;
            n = len(s);

        return True if s[0] == s[1] else False;