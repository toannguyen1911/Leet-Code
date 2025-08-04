from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Rule:
            + Have two baskets, each basket can only hold a single type of fruit.
            + Starting from any tree, must pick exactly one fruit from every tree while moving to the right.
            + Stop when we reach a tree with fruit that cannot fit in your baskets
        """
        
        l = 0;
        max_trees = 1;
        n = len(fruits);
        fruit_count = defaultdict(int)

        for r in range(n):
            fruit_count[fruits[r]] += 1;

            # if we have three fruit types in the baskets
            # we need to remove the first fruit in the baskets
            # repeat until there are exactly two fruit types left in the baskets
            while len(fruit_count) > 2:
                fruit_count[fruits[l]] -= 1;
                if fruit_count[fruits[l]] == 0:
                    del fruit_count[fruits[l]];
                l += 1;
            max_trees = max(max_trees, r - l + 1);

        return max_trees;