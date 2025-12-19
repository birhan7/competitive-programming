class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.left = Node("")
        self.right = Node("", prev=self.left)
        self.left.next = self.right
        self.key_node_map = {}
    
    def length(self):
        return len(self.key_node_map)
    
    def push_right(self, val):
        new_node = Node(val, self.right.prev, self.right)
        self.key_node_map[val] = new_node
        self.right.prev = new_node
        new_node.prev.next = new_node

    def pop_left(self):
        res = self.left.next.value
        self.pop(res)
        return res
    
    def pop(self, val):
        if val in self.key_node_map:
            node = self.key_node_map[val]
            next_node, prev_node = node.next, node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            self.key_node_map.pop(val)
        
    def update(self, val):
        self.key_node_map.pop(val)
        self.push_right(val)


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minlfu = 0
        self.key_value_map = {}
        self.key_count_map = defaultdict(int)
        self.list_map = defaultdict(LinkedList)
    
    def counter(self, key):
        cnt = self.key_count_map[key]
        self.key_count_map[key] += 1
        self.list_map[cnt].pop(key)
        self.list_map[cnt + 1].push_right(key)

        if cnt == self.minlfu and self.list_map[cnt].length() == 0:
            self.minlfu += 1

    def get(self, key: int) -> int:
        if key not in self.key_value_map:
            return -1
        self.counter(key)
        return self.key_value_map[key]
       
    def put(self, key: int, value: int) -> None:
        if key not in self.key_value_map and len(self.key_value_map) == self.capacity:
            removed = self.list_map[self.minlfu].pop_left()
            self.key_value_map.pop(removed)
            self.key_count_map.pop(removed)
        self.key_value_map[key] = value
        self.counter(key)
        self.minlfu = min(self.minlfu, self.key_count_map[key])

        


                
        


            



        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)