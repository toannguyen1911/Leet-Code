class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = emptyBottles = numBottles;

        while (numBottles >= numExchange):
            # Exchange
            ans += 1;
            numBottles = numBottles - numExchange + 1;
            numExchange += 1;

        return ans;