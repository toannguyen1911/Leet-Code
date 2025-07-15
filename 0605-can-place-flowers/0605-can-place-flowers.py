class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pre_planted = 0;
        planted = 0;

        for i in range (len(flowerbed) -1):
            if pre_planted or flowerbed[i] or flowerbed[i +1]:
                pre_planted = flowerbed[i];
                print(i)
                continue;
            planted += 1;
            pre_planted = 1;

        if (not pre_planted and not flowerbed[-1]):
            planted += 1;

        return planted >= n;