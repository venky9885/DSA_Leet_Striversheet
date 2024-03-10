import heapq

# for expln https://www.youtube.com/watch?v=EKZhEN9P2-I
# comments added by  chgpt


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort events by their start time
        events.sort(key=lambda x: x[0])

        # Find the maximum day in the events
        totalDays = max(events[i][1] for i in range(len(events)))
        print(totalDays)  # Debugging line

        day = 0
        pq = []  # Priority queue to store end times of events
        ans = 0  # Counter for the number of attended events
        index = 0  # Index to traverse the events list

        # Iterate through each day from day 0 to totalDays
        while day <= totalDays:
            # Add events that are in progress on the current day to the priority queue
            while index < len(events) and events[index][0] <= day:
                heapq.heappush(pq, events[index][1])
                index += 1

            # Remove events that have already ended (i.e., less than the current day)
            while pq and pq[0] < day:
                heapq.heappop(pq)

            # If there are events available to attend on the current day, attend one
            # even though having mutilpe days we attend 1 only per day
            if pq:
                heapq.heappop(pq)
                ans += 1

            day += 1  # Move to the next day

        return ans  # Return the total number of attended events
