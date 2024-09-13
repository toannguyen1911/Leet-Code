class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        answers = []
        memory = [arr[0]]
        
        # Calculate xor from 0 to index and save to memory
        for index in range (1, len(arr)):
            memory.append(memory[index -1] ^ arr[index]);
        
        # Caluculate the query
        for left, right in queries:
            # if left is 0, the answer is simple an xnor from 0 to right. (memory[right]).
            # otherwise we need to exclude the part of the array before left.
            answer = memory[right] if left == 0 else memory[right] ^ memory[left -1]
            answers.append(answer)
        return answers;