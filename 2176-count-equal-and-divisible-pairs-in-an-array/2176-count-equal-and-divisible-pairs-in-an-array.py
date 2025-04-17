class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        def bruteForce():
            n = len(nums);
            ans = 0;
            for i in range (n -1):
                for j in range (i +1, n):
                    if (nums[i] == nums[j] and ((i * j) % k == 0)):
                        ans += 1;
            return ans;

        def optimized():
            '''
                We just need to check for the same numbers.
                So group them together
            '''
            mem = defaultdict(list);
            ans = 0;

            # Step 1: Group Genins (numbers) by village (same value)
            for i, val in enumerate(nums):
                # Step 2: Check only within the same group (same number)
                for j in mem[val]:
                    if (i * j) % k == 0:
                        ans += 1;
                # Step 3: Add current index to the list of indices for the number
                mem[val].append(i);
            
            return ans;

        # return bruteForce();
        return optimized();
        