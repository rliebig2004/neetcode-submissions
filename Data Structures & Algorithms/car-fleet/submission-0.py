class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # fleet only formed if car[i - 1] takes longer than car[i]
        # car doesn't catch up if takes the same or less time as the front of it (no fleet)

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        fleets = 1

        prevTime = (target - pair[0][0]) / pair[0][1]
        for i in range(1, len(pair)):
            
            currCar = pair[i]
            currTime = (target - pair[i][0]) / pair[i][1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime

        return fleets


            
