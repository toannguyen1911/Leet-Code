class Solution(object):
    def maxFreqSum(self, s):
        freq = [0] * 26;
        max_v, max_c = 0, 0;

        for c in s:
            i = ord(c) - ord('a');
            freq[i] += 1;

            if c in 'aeiou':
                max_v = max(max_v, freq[i]);
            else:
                max_c = max(max_c, freq[i]);

        return max_v + max_c;