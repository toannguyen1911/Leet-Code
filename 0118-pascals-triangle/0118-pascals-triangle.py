class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [];
        for i in range(numRows):
            row = [];
            for j in range(i +1):
                val = 1 if j == 0 or j == i else triangle[i -1][j -1] + triangle[i -1][j];
                row.append(val);
            triangle.append(row);

        return triangle;
