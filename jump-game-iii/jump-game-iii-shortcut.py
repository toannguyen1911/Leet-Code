class Solution:
    
    def canReach(self, arr: List[int], start: int) -> bool:
        return jump(start, arr)

def jump(index, arr):
        
    if index >= 0 and index < len(arr) and arr[index] != None:
        val = arr[index]
        arr[index] = None
        if val == 0:
            return True
        return jump(index + val, arr) or jump(index - val, arr)
    return False
