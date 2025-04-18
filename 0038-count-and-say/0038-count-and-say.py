class Solution:
    
    def runLengthEncoding(self, s: str) -> str:
        output = ''
        count = 1  
    
        for i in range(1, len(s)):
            # If the current character is the same as the previous one
            if s[i] == s[i - 1]: 
                count += 1;
            else:
                # Add previous character and its count to output
                output += f"{count}{s[i - 1]}";
                count = 1;
        
        # After the loop, we still need to add the last character group
        output += f"{count}{s[-1]}";
        
        return output;

    def countAndSay(self, n: int) -> str:
        # base case
        if n <= 1:
            return '1';

        rle = self.countAndSay(n -1);
        rle = self.runLengthEncoding(rle);

        print(rle)
        return rle;