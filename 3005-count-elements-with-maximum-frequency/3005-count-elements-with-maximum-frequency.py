class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ans = 0;
        max_freq = 0;
        freqs = {};

        for num in nums:
            freq = freqs.get(num, 0) +1;
            freqs[num] = freq;
            if (freq > max_freq):
                max_freq = freq;
        
        for num in nums:
            if freqs[num] == max_freq:
                ans += 1;
    
        return ans;