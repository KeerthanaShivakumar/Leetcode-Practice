#478 - Generate random point in circle
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        angle = (random.uniform(0,1))*2*math.pi
        hyp= sqrt(random.uniform(0,1))*self.radius
        adj = cos(angle)*hyp
        opp = sin(angle)*hyp
        return((self.x_center+adj), (self.y_center+opp))

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()