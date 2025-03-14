class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        ans = 0;
        l, r = 1, max(candies);

        # Use binary search
        # Check with mid, calculate how many children can receive mid candies
        while (l <= r):
            mid = (l + r) // 2;
            children_count = sum(pile // mid for pile in candies)
            
            if children_count >= k:
                ans = mid if mid > ans else ans
                l = mid + 1
            else:
                r = mid - 1
                
        return ans;