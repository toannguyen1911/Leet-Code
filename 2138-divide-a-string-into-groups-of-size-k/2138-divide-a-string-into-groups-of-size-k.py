class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = [];
        string = '';
        count = 0;

        for c in s:
            string += c;
            count += 1;
            if count >= k:
                ans.append(string);
                string = "";
                count = 0;
        
        if count < k and count != 0:
            string += (fill * (k - count));
            ans.append(string);
        return ans;
