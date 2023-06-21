class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        #print(len(nums), k)
        if k ==0:
            return nums
        if len(nums) <= 2*k:
            return [-1] * len(nums)

        result = [-1] *k
        S = sum(nums[: 2*k +1])
        
        if S != 0:
                result.append(S // (2 *k +1))
        else: result.append(S)
        #print(S)
        for index in range(k +1, len(nums) -k):
            S = S -nums[index -k -1] + nums[index +k] 
            #print(S)
            if S != 0:
                #print(sum(nums[index -k: index +k +1]))
                result.append(S // (2 *k +1))
            else: result.append(S)
        result += [-1] *k
        return result