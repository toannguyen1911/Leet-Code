class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = "";
        temp = "";
        count = 0;
        n1, n2 = len(str1), len(str2);

        for c in str1:
            temp += c;
            count += 1;

            if count > n1 or count > n2:
                return ans;
            if temp * (n1 // count) == str1 and temp * (n2 // count) == str2:
                ans = temp;

        return ans;