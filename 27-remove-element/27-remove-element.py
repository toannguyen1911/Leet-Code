class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        while(1):
            try:
                nums.remove(val)
                #nums.append("_")
                count += 1
            except:
                return len(nums)#len(nums) - count#, count]
        return len(nums)
        