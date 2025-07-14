class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        ans = 0;

        players.sort();
        trainers.sort();
        i, j = 0, 0;
        n, m = len(players), len(trainers);

        while (True):
            if i >= n or j >= m:
                return ans;

            if players[i] <= trainers[j]:
                i += 1;
                ans += 1;
            j += 1; 

        return ans;
