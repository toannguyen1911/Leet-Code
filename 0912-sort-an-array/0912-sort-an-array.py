class Solution:
    # Merge two array
    def mergeArray(self,l_array, r_array):
          l = 0
          r = 0
          result = []
          while (1):
            if l_array[l] < r_array[r]:
              result.append(l_array[l])
              if (l + 1 >= len(l_array)):
                return result + r_array[r:]
              l += 1
              continue

            result.append(r_array[r])
            if (r + 1 >= len(r_array)):
              return result + l_array[l:]
            r += 1

    #devide array to two sub-array
    def mergeSort(self,nums, left, right):
      if (left == right):
        return [nums[left]]

      center = (right + left ) // 2
      l_array = self.mergeSort(nums, left, center)
      r_array = self.mergeSort(nums, center + 1, right)

      return self.mergeArray(l_array, r_array)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums) -1)
        
        
