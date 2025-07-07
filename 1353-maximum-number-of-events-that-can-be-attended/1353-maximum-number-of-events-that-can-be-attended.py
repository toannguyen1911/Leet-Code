import heapq

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort();
        ans = 0;
        i = 0;
        n = len(events);
        
        # Min-heap to track events by their end day
        min_heap = [];
        
        # Determine the last day we need to simulate
        last_day = max(end for _, end in events);

        # Simulate each day
        for day in range(1, last_day + 1):
            # SAdd all events starting today to heap
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1]);
                i += 1;

            # Remove events that already ended
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap);

            # Attend the event that ends earliest
            if min_heap:
                heapq.heappop(min_heap);
                ans += 1;

            # Break early if no events remain
            if i == n and not min_heap:
                break;

        return ans;