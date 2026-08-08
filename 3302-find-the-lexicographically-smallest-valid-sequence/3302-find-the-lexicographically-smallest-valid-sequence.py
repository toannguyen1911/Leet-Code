class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        """
            - Pre-build suffix match counts from right to left.
            - Greedily match word2 and use one allowed mismatch when possible.

            Time complexity: O(n + m)
            Space complexity: O(n)
        """

        n, m = len(word1), len(word2);
        matched = 0;
        r = m -1; # word2 position
        suffix = [0] *n;

        for i in range(n -1, -1, -1):
            suffix[i] = matched;

            if r >= 0 and word1[i] == word2[r]:
                r -= 1;
                matched += 1;

        res = [];
        j = 0;
        changed = False;
        
        for i in range(n):
            if j >= m:
                break;
            
            if word1[i] == word2[j]:
                res.append(i);
                j += 1;
            elif not changed and suffix[i] >= m - 1 - j:
                # Use the one allowed change at position i
                res.append(i);
                j += 1;
                changed = True;
        
        return res if j == m else [];