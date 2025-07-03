class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a";
        index = 1;

        while (index < k):
            for c in word:
                index += 1;
                next_c = chr(ord(c) + 1);
            
                if (index == k):
                    return next_c;
                word += next_c;
    
        return word;