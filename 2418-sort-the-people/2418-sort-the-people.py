class Solution:
        
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Implement Bubble Sort
        for i in range(len(names) -1):
            for j in range(i +1, len(names)):
                if (heights[i] < heights[j]):
                    heights[i], heights[j] = heights[j], heights[i]
                    names[i], names[j] = names[j], names[i]
        return names
        