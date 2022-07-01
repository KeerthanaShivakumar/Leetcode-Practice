#1710. Maximum Units on a Truck - Easy
'''
Approach- use Greedy technique to maximize the number of units loaded into truck
Similar to Knapsack Problem (Standard Problem)
'''
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        #reverse them in decreasing order of units to maximize units
        result = 0
        for box, units in boxTypes:
            #do until the trucksize is greater than boxsize
            if truckSize >= box:
                truckSize -= box #reduce truck size by number of boxes taken
                result += box * units #calculate units
            else:
                result += truckSize * units #final case when the trucksize is lesser than boxsize taken
                break
        return result
    