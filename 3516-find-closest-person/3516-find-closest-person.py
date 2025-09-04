class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dist_1 = abs(x -z);
        dist_2 = abs(y -z);

        if dist_1 == dist_2:
            return 0;
        if dist_1 < dist_2:
            return 1;
        return 2;