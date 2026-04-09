class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #4:2 6:2 8:2
        #1:2 3:2 5:2
        #0:1
        #7:1 8:1
        cars = list(zip(position, speed))
        fleets = 0
        curr_max_time = 0
        cars.sort(reverse = True)
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > curr_max_time:
                fleets += 1
                curr_max_time = time
        return fleets





