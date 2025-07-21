class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = "";
        flag = s[0];
        count = 0;

        for c in s:
            if c != flag:
                flag = c;
                count = 1;
                ans += c;
                continue;
            count += 1;
            if (count < 3):
                ans += c;

        return ans; 