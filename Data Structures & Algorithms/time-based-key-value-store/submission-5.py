class TimeMap:

    def __init__(self):
        self.hold = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hold:
            self.hold[key] = []
        self.hold[key].append((timestamp, value))
        #alice: 1, happy
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hold:
            return ""
        arr = self.hold[key]
        #1, happy. 3, angry.
        answer = ""
        L = 0
        R = len(arr) - 1
        while L <= R:
            mid = (L + R) // 2
            if arr[mid][0] <= timestamp:
                answer = arr[mid][1]
                L += 1
            else:
                R -= 1
        return answer

        



        
