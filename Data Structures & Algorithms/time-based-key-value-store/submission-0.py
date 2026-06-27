class TimeMap:
    def __init__(self):
        # dictionary mapping key -> list of (timestamp, value)
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key not in store, initialize empty list
        if key not in self.store:
            self.store[key] = []
        # append (timestamp, value) pair
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # if key not found, return empty string
        if key not in self.store:
            return ""
        # iterate backwards to find latest timestamp <= given timestamp
        for t, v in reversed(self.store[key]):
            if t <= timestamp:
                return v
        return ""