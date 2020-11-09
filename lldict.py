import time

class _LLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.key) + ": " + str(self.value)

class LLDictionary:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, key):
        return not self._find(self._head, key) is None

    def __getitem__(self, key):
        node = self._find(self._head, key)
        if node == None:
            raise KeyError("Item does not exist")
        return node.value

    def _find(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        else:
            return self._find(node.next, key)

    def __setitem__(self, key, value):
        if self._head == None:
            self._head = _LLNode(key, value)
            self._size += 1
        else:
            self._insert(self._head, key, value)

    def _insert(self, node, key, value):
        if node.key == key:
            node.value = value
        else:
            if node.next is not None:
                self._insert(node.next, key, value)
            else:
                node.next = _LLNode(key, value)
                self._size += 1

    def _remove(self, node, prevnode, key):
        assert node is not None, "Cannot remove non-existent key."
        if key != node.key:
            node.next = self._remove(node.next, node, key)
        else:
            if node == self._head:
                self._head = node.next
            else:
                prevnode.next = node.next
            temp = node
            node = None
            self._size -= 1
        return temp

    def pop(self, key):
        value = self[key]
        self._remove(self._head, key)
        return value

    def print_dict(self):
        if self._head is not None:
            self._print_dict(self._head)

    def _print_dict(self, node):
        if node is not None:
            print(node)
            self._print_dict(node.next)

def main():
    dict = LLDictionary()
    for i in range(1,100):
        dict[i] = "Jack" + str(i)

    start_time = time.time()
    results = 99 in dict
    print("searching 99: --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    results = 20 in dict
    print("searching 20: --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    dict[100] = "Jack22"
    print("inserting 100: --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    dict[-10] = "Jack-10"
    print("inserting -10: --- %s seconds ---" % (time.time() - start_time))

    print(len(dict))
    dict.print_dict()

if __name__ == "__main__":
    main()
