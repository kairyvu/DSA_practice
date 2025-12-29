class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left
        self.map = {}
    
    def length(self):
        return len(self.map)
    
    def addNode(self, val):
        newNode = Node(val, self.right, self.right.prev)
        self.map[val] = newNode
        self.right.prev = newNode
        newNode.prev.next = newNode
    
    def removeNode(self, val):
        if val not in self.map:
            return
        node = self.map[val]
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        del self.map[val]

    def popLeft(self):
        val = self.left.next.val
        self.removeNode(val)
        return val

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2val = {}
        self.count2map = defaultdict(LinkedList) # count -> LinkedList
        self.key2count = defaultdict(int) # key -> count
        self.lfu = 0

    def updateCount(self, key):
        count = self.key2count[key]
        self.count2map[count].removeNode(key)
        self.count2map[count + 1].addNode(key)
        self.key2count[key] += 1

        if count == self.lfu and self.count2map[count].length() == 0:
            self.lfu += 1

    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        self.updateCount(key)
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key2val:
            self.key2val[key] = value
            self.updateCount(key)
            return

        if len(self.key2val) == self.capacity:
            oldKey = self.count2map[self.lfu].popLeft()
            del self.key2val[oldKey]
            del self.key2count[oldKey]

        self.key2val[key] = value
        self.key2count[key] = 1
        self.count2map[1].addNode(key)
        self.lfu = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)