class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # In this problem count the frequency
        d = {}
        for i in tasks:
            if(i in d):
                d[i] += 1
            else:
                d[i] = 1
        # max heap is not present so we make  negatives
        maxHeap = [-1*v for v in d.values()]
        time = 0
        heapq.heapify(maxHeap)
        q = deque()
        print(maxHeap)
        while (maxHeap or q):
            time += 1
            # if maxheap present then decrement and add it to qiueue
            if(maxHeap):
                p = 1+heapq.heappop(maxHeap)
                if(p):
                    print(p, n+time)
                    q.append((p, n+time))
            # get one number from queue and make it to wait until its time comes that is current time + idle wait time
            if(q and q[0][1] == time):
                # after getting decrement it and again add it to maxheap
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
