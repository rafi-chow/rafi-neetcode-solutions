class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #4:2 6:2 8:2
        #1:2 3:2 5:2
        #0:1
        #7:1 8:1
        stack = []
        output = 0
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        current_max_time = 0
        for pos, spd, in cars:
            #1:3 4:3 7:3 10:3
            #4:2 6:2 8:2 10:2 #position same, so same fleet
            time = (target - pos) / spd
            if time > current_max_time:
                output += 1
                current_max_time = time
            elif time <= current_max_time:
                continue
        return output
                



