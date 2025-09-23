class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.');
        ver2 = version2.split('.');
        i, n, m = 0, len(ver1), len(ver2);

        while (i < n or i < m):
            num1 = int(ver1[i]) if i < n else 0;
            num2 = int(ver2[i]) if i < m else 0;
            i += 1;

            if num1 < num2:
                return -1;
            if num1 > num2:
                return 1;
        return 0;