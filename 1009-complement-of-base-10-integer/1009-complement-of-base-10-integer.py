class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n = list(bin(n))
        for i in range(len(n)):
            if n[i] == "b":
                for j in range(i+1, len(n)):
                    if n[j] == "0":
                        n[j] = "1"
                    else: n[j] = "0"
        n = ''.join(n)
        return int(n, 2) 
        