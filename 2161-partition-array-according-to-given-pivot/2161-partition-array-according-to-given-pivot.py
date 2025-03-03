class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = [];
        more = [];
        equal = [];

        for num in nums:
            if (num < pivot):
                less.append(num);
            if (num > pivot):
                more.append(num);
            if (num == pivot):
                equal.append(num);
        return less + equal + more;