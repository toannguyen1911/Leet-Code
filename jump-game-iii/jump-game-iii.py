class Solution:
    
    def canReach(self, arr: List[int], start: int) -> bool:
        return jump(start, arr)

def jump(index, arr):
        #print(arr, index)
        if index < 0 or index >= len(arr):
            return False
        val = arr[index]
        arr[index] = None
        if val == 0:
            return True
        elif val == None:
            return False
        a = jump(index + val, arr)
        #print(a)
        if a: return True
        b = jump(index - val, arr)
        #print(b)
        if b: return True
        return False