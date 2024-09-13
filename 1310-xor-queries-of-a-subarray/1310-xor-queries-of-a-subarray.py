class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        memories = {}
        result = [];
        for query in queries:
            key = str(query[0]) + '-' + str(query[1]);
            if (key in memories.keys()):
                result.append(memories[key]);
                continue;
            flag = arr[query[0]];
            for index in range (query[0] + 1, query[1] +1):
                # print(flag, index)
                flag ^= arr[index]
            memories[key] = flag;
            result.append(flag)
        # print(memories);
        return result;