class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort()

        n = len(cars)
        res = n
        timeTravelFleetHead = (target - cars[-1][0]) / cars[-1][1]
        
        for i in range(n - 2, -1, -1):
            currTimeToTarget = (target - cars[i][0]) / cars[i][1]
            if currTimeToTarget <= timeTravelFleetHead:
                res -= 1
            else:
                timeTravelFleetHead = currTimeToTarget
        return res