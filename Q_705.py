#Q705 - Design a HashSet without using any built-in hash table libraries.
class MyHashSet:

    def __init__(self):
        #assume set is the list here
        self.set=[False]*1000001 #all elements in the set are initially absent

    def add(self, key: int) -> None:
        self.set[key]=True #elements are present in the given key

    def remove(self, key: int) -> None:
        self.set[key]=False #elements are removed from the given key

    def contains(self, key: int) -> bool:
        return self.set[key] #show if element is present or not


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)