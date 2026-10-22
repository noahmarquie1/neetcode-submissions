class LRUCache:

    def __init__(self, capacity: int):
        self.use_order: [int] = []
        self.cache: dict[int, int] = {}
        self.capacity: int = capacity
        
    def size(self):
        return len(self.cache.keys())

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.use_order.remove(key)
            self.use_order.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Handles key moving
        if key in self.use_order:
            # Need to move key up in use order
            self.use_order.remove(key)
        self.use_order.append(key)

        # Handle putting key in, and removing an item if necessary
        self.cache[key] = value
        if self.size() > self.capacity:
            lru_key = self.use_order.pop(0)
            self.cache.pop(lru_key)

            

        
