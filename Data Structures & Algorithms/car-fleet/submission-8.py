class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #4:2 6:2 8:2
        #1:2 3:2 5:2
        #0:1
        #7:1 8:1
        cars = list(zip(position,speed))
        curr = 0
        output = 0
        cars.sort(reverse=True)
        for pos, spd in cars:
            time = (target - pos) / spd
            #8 : 2: 1
            #6 : 3: 1
            if time > curr:
                curr = time
                output += 1
        return output




