class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1;
        self.nums2 = nums2;
        self.freq = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        num = self.nums2[index];
        self.freq[num] -= 1;
        self.freq[num + val] = self.freq.get(num + val, 0) + 1;
        self.nums2[index] += val;

    def count(self, tot: int) -> int:
        count = 0;
        for num in self.nums1:
            count += self.freq.get(tot - num, 0);
        return count;
        
    def frequency(self, nums1: List[int], nums2: List[int]) -> None:
        freq = {};
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                val = nums1[i] + nums2[j];
                freq[val] = freq.get(val, 0) + 1;
        
        return freq;

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)