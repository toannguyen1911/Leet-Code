class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        temp = []
        if numRows <= 2:
            for i in range(numRows):
                result.append([1]* (i + 1))
        else:
            result = [[1], [1, 1]]
            for index in range(2, numRows):
                for j in range(1, index):
                    temp.append(result[index -1][j -1] + result[index -1][j])
                #print([1] + temp + [1])
                result.append([1] + temp + [1])
                temp = []
        return result
                
        