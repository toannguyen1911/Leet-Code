import math

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = 0
        memory = [0] * 26
        # first char is 97
        for char in word:
            memory[ord(char) - 97] += 1
        memory.sort(reverse = True)
        
        for i in range (len(memory)):
            if (memory[i] != 0):
                count += (math.ceil((i + 1) / 8) * memory[i])
            
        return count