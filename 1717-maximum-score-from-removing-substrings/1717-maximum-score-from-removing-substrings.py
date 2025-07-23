class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        - Operation: 
        + Remove "ab" and gain x points
        + Remove "ba" and gain y points
        - Return: max point
        """
        def solve(score, max_s, points):
            stack = [];

            for c in s:
                if not stack:
                    stack.append(c);
                    continue;
                if stack[-1] + c == max_s:
                    score += points;
                    stack.pop();
                    continue;
                stack.append(c);
            return "".join(stack), score;
        
        ans = 0;

        if x >= y:
            s, ans = solve(ans, "ab", x);
            s, ans = solve(ans, "ba", y);
        else:
            s, ans = solve(ans, "ba", y);
            s, ans = solve(ans, "ab", x);
        return ans;
