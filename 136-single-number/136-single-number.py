class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = Counter(nums)
        #print(list(a))
        for i in list(a):
            #print(i)
            if a[i] == 1:
                return i
        