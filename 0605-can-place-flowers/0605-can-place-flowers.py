class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k = len(flowerbed);

        if n == 0:
            return True;

        for i in range (k):
            if (i == 0 or not flowerbed[i -1]) and not flowerbed[i] and (i == k -1 or not flowerbed[i +1]):
                flowerbed[i] = 1;
                n -= 1;
                if n == 0:
                    return True;
        return False;