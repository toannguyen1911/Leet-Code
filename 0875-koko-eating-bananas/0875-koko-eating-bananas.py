class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
            Input:
            - n piles of bananas: int
            - h hours: int -> time for the guards to back
            - k: int -> eating speed of per hour
            Output:
            - min(k) -> eat all the bananas within h hours
            Note:
            - If the pile < k bananas, eats all of them instead and will not eat any more bananas during this hour.
        """

        # Define search range:
        left = 1;
        right = max(piles);

        """
            Helper function:
            - Check if Koko can eat all the bananas within h hours?
        """
        def can_eat_all(k):
            times = 0;
            i = 0;
            bananas = piles[i];
            
            while (times < h):
                times += 1;
                bananas -= k;
                if (bananas <= 0 and i +1 < len(piles)):
                    i += 1;
                    bananas = piles[i];
                
                if (bananas <= 0):
                    return True;

            return False;


        while (left < right):
            mid = (left + right) // 2;
            
            if (can_eat_all(mid)):
                right = mid;
            else:
                left = mid + 1;
        return left;