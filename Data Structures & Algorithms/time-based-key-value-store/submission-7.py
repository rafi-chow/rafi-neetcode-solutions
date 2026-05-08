class TimeMap:

    def __init__(self):
        self.hold = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hold:
            self.hold[key] = []
        self.hold[key].append((timestamp, value))
        #alice: 1, happy
        #alice: 3, sad
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hold:
            return ""
        arr = self.hold[key] #(1, happy) #(3, sad)
        res = ""
        L = 0
        R = len(arr) - 1

        while L <= R:
            mid = (L + R) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                L = mid + 1
                res = arr[mid][1]
            else:
                R = mid - 1

        return res


        



        
