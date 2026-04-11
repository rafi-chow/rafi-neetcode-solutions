class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #4:2 6:2 8:2
        #1:2 3:2 5:2
        #0:1
        #7:1 8:1
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        longest = 0
        output = 0
        for i in range(len(position)):
            curr = (target - cars[i][0]) / cars[i][1]
            #1 1 12 
            if curr > longest:
                output += 1
                longest = curr
        return output
        





