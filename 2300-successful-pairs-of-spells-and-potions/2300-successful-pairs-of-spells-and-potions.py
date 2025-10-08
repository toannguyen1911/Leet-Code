class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = [];
        n = len(potions);

        # Prepare for binary search 
        potions.sort();

        for spell in spells:
            # Binary search for first successful potion
            l, r = 0, n -1;
            while (l <= r):
                m = (l + r) //2;
                if potions[m] * spell < success:
                    l = m + 1;
                else: r = m -1;
            ans.append(n - l);
        return ans;