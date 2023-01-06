class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res=0
        costs = sorted(costs)
        for cost in costs:
            if(cost<=coins):
                res+=1
                coins = coins - cost
        return res