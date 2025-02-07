from collections import defaultdict
from collections import Counter

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = [];
        ball_map = defaultdict(str);
        color_freq = Counter();
        
        for ball, color in queries:
            # remove old color
            if (ball_map[ball] != ''):
                old_color = ball_map[ball];
                color_freq[old_color] -= 1;
                # del color if count equal zero
                if color_freq[old_color] == 0:
                    del color_freq[old_color]
            # add new color for ball
            ball_map[ball] = color
            color_freq[color] += 1;
            ans.append(len(color_freq));

        return ans;
        