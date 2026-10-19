class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cash = {}  # key -> Node
        # Dummy nodes for boundary markers
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev   

    def insert(self, node: Node) -> None:
        # Inserts node right before dummy right node (Most Recently Used position)
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cash:
            # Move accessed node to the most recently used position
            node = self.cash[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cash:
            self.remove(self.cash[key])
            
        # Create and insert the new node
        new_node = Node(key, value)
        self.cash[key] = new_node
        self.insert(new_node)

        # Evict Least Recently Used (LRU) node if over capacity
        if len(self.cash) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cash[lru.key]