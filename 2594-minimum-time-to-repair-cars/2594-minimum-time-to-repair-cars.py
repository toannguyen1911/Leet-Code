class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """
            Input: 
            - ranks: array, ranks[i] is the rank of i-th mechanic
            A mechanic rank r can repair n cars in r * n^2 minutes
            - cars: interger
            Output:
            - min time taken to repair all the cars
            Note: All the mechanics can repair the cars simultaneously.
        """

        # Define the search range: 
        # min 1m, max is the time of best mechanic
        left = 1;
        right = min(ranks) * cars * cars 

        """
            Helper function:
            - Check if we can repair all the cars in time "t"?
        """
        def can_repair_all_cars(t):
            repaired = 0;

            for r in ranks:
                # r * n * n = t
                n = int((t / r) ** 0.5);
                repaired += n;
                if repaired >= cars:
                    return True;
            return False;

        # Use binary search, with mid time, can we repaired all cars
        while (left < right):
            mid = (left + right) // 2;
            if can_repair_all_cars(mid):
                right = mid;
            else: 
                left = mid +1;
        return right; 
