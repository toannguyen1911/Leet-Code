class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        c = Counter(nums)
        
        if k == 0:
            for key, v in c.items():
                if v > 1:
                    count += 1
        else:
            for key, v in c.items():
                if key + k in c:
                    count += 1
        return count
    #copy