class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0;
        n = len(bank);
        devices = [];

        for row in bank:
            r = list(map(int, list(row)));
            devices.append(sum(r));

        pre = 0;
        for row in devices:
            if row != 0:
                res += pre * row;
                pre = row;
     
        return res;