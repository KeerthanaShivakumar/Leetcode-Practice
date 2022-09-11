#Q_1383 - Maximum Performance in a Team

import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng=[]
        for eff, spd in zip(efficiency, speed):
            eng.append([eff,spd])
        eng.sort(reverse=True)
        res=0
        speed=0
        minHeap = []
        for eff,spd in eng:
            if(len(minHeap)==k):
                speed = speed-heapq.heappop(minHeap)
            speed=speed+spd
            heapq.heappush(minHeap,spd)
            res = max(res, speed*eff)
        return (res%(10**9+7))