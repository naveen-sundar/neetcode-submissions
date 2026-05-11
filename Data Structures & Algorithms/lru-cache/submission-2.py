class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next, self.prev = None, None;



class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity;
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, Node): # Insert at right
        Node.prev = self.right.prev

        self.right.prev.next = Node
        self.right.prev = Node
        Node.next = self.right



    def delete(self, node): # Delete the lru cache
        p, cur = node.prev, node.next
        p.next = cur
        cur.prev = p 
    
    def get(self, key: int) -> int: # return value of the corresponding key
        

        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        # Insert node at right

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.delete(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        lru = self.left.next
        if len(self.cache) > self.cap:
            self.delete(lru)
            del self.cache[lru.key]
