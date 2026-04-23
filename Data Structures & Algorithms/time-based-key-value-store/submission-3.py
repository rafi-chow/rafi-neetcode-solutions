class TimeMap:

    def __init__(self):
        self.hold = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hold:
            self.hold[key] = []
        self.hold[key].append((timestamp, value))
            #1: alice: 1, happy
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hold:
            return ""
        arr = self.hold[key]
        #[(1, "bar"), (4, "bar2")]
        L = 0
        R = len(arr) - 1 #1
        answer = ""

        while L <= R:
            mid = (L + R) // 2 #0

            if arr[mid][0] <= timestamp:
                answer = arr[mid][1]
                L = mid + 1
            else:
                R = mid - 1
        return answer

        
