class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        res = 0
        count = 1
        mark = 0

        def compress_char(c: str, length: int, mark: int, count: int):
            chars[mark] = c
            mark += 1
            length += 1

            if count > 1:
                for num in str(count):
                    chars[mark] = num
                    mark += 1
                    length += 1

            return length, mark

        for i in range(n - 1):
            if chars[i] == chars[i + 1]:
                count += 1
                continue

            res, mark = compress_char(chars[i], res, mark, count)
            count = 1

        # Handle the last character/group
        res, mark = compress_char(chars[-1], res, mark, count)
        return res
