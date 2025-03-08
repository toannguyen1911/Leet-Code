class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # find substring have largest number black block
        ans = 0;
        count = blocks[:k].count('B');

        for i in range (len(blocks) - k ):
            count += 0 if blocks[i] == blocks[i + k] else (1 if blocks[i] == 'W' else -1);
            if count > ans:
                ans = count;
        return k - ans;