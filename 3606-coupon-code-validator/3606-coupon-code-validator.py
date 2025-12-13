class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        """
        Time complexity: O(n);
        Space complexity: O(n);
        """
        validLines = ["electronics", "grocery", "pharmacy", "restaurant"];
        buckets = {line: [] for line in validLines};

        def isValidCode(s):
            return bool(s) and all(c.isalnum() or c == "_" for c in s);

        for c, line, active in zip(code, businessLine, isActive):
            if not active:
                continue;
            if not isValidCode(c):
                continue;
            if line not in validLines:
                continue;

            buckets[line].append(c);
        
        res = [];
        for line in validLines:
            res.extend(sorted(buckets[line]));
        return res;