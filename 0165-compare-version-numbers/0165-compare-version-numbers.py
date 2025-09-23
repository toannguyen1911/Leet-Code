class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.');
        ver2 = version2.split('.');
        i, n, m = 0, len(ver1), len(ver2);

        while (i < n or i < m):
            if i >= n :
                a = 0;
                b = ver2[i];
            elif i >= m:
                b = 0;
                a = ver1[i];
            else: a, b =  ver1[i], ver2[i];
            i += 1;

            a = int (a);
            b = int(b);
            if a < b:
                return -1;
            if a > b:
                return 1;

        return 0;