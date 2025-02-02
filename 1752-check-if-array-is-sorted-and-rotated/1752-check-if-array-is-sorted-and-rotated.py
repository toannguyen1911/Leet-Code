class Solution(object):
    def check(self, nums):
        flag = None;

        for i in range (len(nums)):
            if i == len(nums) -1:
                if flag != None and nums[i] > nums[0]:
                    return False;
                return True;
            if (flag != None and (nums[i] > nums[i + 1] or nums[i] > nums[0])):
                    return False;
            if nums[i] > nums[i +1]:
                flag = nums[i];

        return True;