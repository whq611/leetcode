class LRUCache:

    def __init__(self, capacity: int):
        self.a_list = []
        self.a_dic = {}
        self.len = capacity

    def get(self, key: int) -> int:
        if key in self.a_dic:
            self.a_list.remove(key)
            self.a_list.append(key)
            return self.a_dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.a_dic:
            self.a_dic[key] = value
            self.a_list.remove(key)
            self.a_list.append(key)
        else:
            if len(self.a_list) == self.len:
                b = self.a_list.pop(0)
                del self.a_dic[b]
            self.a_list.append(key)
            self.a_dic[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
