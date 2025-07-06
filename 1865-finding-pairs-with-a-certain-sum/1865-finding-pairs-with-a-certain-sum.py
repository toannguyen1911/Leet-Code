class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = sorted(nums1);
        self.nums2 = nums2;
        self.freq = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        num = self.nums2[index];
        self.freq[num] -= 1;
        self.freq[num + val] = self.freq.get(num + val, 0) + 1;
        self.nums2[index] += val;

    def count(self, tot: int) -> int:
        ans = 0;
        for num1 in self.nums1:
            if num1 > tot:
                break;
            ans += self.freq.get(tot - num1, 0);
        return ans;

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)