class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        arr = [[float('inf')] * 26 for _ in range(26)]
        
        for i in range(26):
            arr[i][i] = 0
        
        for i in range(len(original)):
            fr = ord(original[i]) - ord('a')
            to = ord(changed[i]) - ord('a')
            arr[fr][to] = min(arr[fr][to], cost[i])
        
        for i in range(26):
            for j in range(26):
                for k in range(26):
                    arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])
        
        answer = 0
        for i in range(len(source)):
            fr = ord(source[i]) - ord('a')
            to = ord(target[i]) - ord('a')

            if fr == to:
                continue

            if arr[fr][to] == float('inf'):
                return -1
            
            answer += arr[fr][to]
        
        return answer