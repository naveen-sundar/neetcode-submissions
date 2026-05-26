class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canShip(capacity):
            remaining = capacity
            containers = 1
            for i in weights:
                if remaining - i < 0:
                    containers += 1
                    remaining = capacity
                remaining = remaining - i
            return containers <= days
        
        low, high = max(weights), sum(weights)
        res = high
        while low <= high:
            
            capacity = (low + high) // 2
            if canShip(capacity):
                res = min(res, capacity)
                high = capacity - 1
            else:

                low = capacity + 1
        
        return res