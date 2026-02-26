class Solution:
    def numSteps(self, s: str) -> int:
        res = 0;
        num = int(s, 2);

        while (True):
            if num == 1:
                break;
            if math.log2(num).is_integer():
                res += int(math.log2(num));
                break;
            res += 1;
            num = num + 1 if num % 2 else num // 2;

        return res;