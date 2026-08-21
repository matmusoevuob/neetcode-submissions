class Node:
    def __init__(self, key=-1, value=-1) -> None:
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.bucket_size = 1000
        self.linked_list_array = [Node() for _ in range(self.bucket_size)]

    def _find_hash_bucket(self, key):
        return self.linked_list_array[key % self.bucket_size]

    def put(self, key: int, value: int) -> None:
        head = self._find_hash_bucket(key)
        while head.next:
            if head.next.key == key:
                head.next.value = value
                return
            head = head.next

        head.next = Node(key, value)

    def get(self, key: int) -> int:
        head = self._find_hash_bucket(key)
        while head:
            if head.key == key:
                return head.value
            head = head.next # BUG: forgot this
        return -1

    def remove(self, key: int) -> None:
        head = self._find_hash_bucket(key)

        if head.key == key:
            next_node = head.next
            head.next = None
            dummy = Node()
            dummy.next = next_node 
            return

        while head and head.next:
            if head.next.key == key:
                head.next = head.next.next
                return 
            head = head.next




# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)