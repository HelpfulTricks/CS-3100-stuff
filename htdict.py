class HTDictionary:

    def __init__(self, arr, size):
        self._max_size = 20
        self._hash_table = [[] for _ in range(0, self._max_size)]
        for i in arr:
            self._hash_table[self._hash_function(i[0])-1].append(i)
        self._size = len(arr)

    def _hash_function(self, key):
        return key % self._max_size

    def __len__(self):
        return self._size

    def _find(self, key):
        for i, j in enumerate(self._hash_table):
            for k, l in enumerate(j):
                if l[0] == key:
                    return [i, k]
        return -1

    def __contains__(self, key):
        results = self._find(key)
        if results == -1:
            return False
        return True

    def __getitem__(self, key):
        item = self._find(key)
        if item == -1:
            raise KeyError("Item does not exist")
        return self._hash_table[item[0]][item[1]]

    def __setitem__(self, key, value):
        self._insert(key,value)

    def _insert(self, key, value):
        item = self._find(key)
        if item == -1:
            self._hash_table[self._hash_function(key)-1].append([key, value])
            self._size += 1
        else:
            self._hash_table[item[0]][item[1]] = [key, value]

    def pop(self, key):
        item = self._find(key)
        if item == -1:
            raise KeyError("Item does not exist")
        else:
            self._hash_table[item[0]].pop(item[1])
            self._size -= 1

    def __str__(self):
        results = ""
        for entry in self._hash_table:
            if len(entry) != 0:
                for x in entry:
                    results+= "Key: " + str(x[0]) + " value: " + x[1]
                    results += "\n"
        results += "Length: " + str(self._size)
        return results

def main():
    arr = [[1,"John"],[3,"Jack"],[2, "Ann"], [21, "Amy"]]
    dict = HTDictionary(arr, 20)
    # Printing original dictionary
    print(dict)
    # Changing the entry at key 1 in the dictionary
    dict[1] = "Ted"
    print(dict)
    # Removing the entry at key in the dictionary
    dict.pop(1)
    print(dict)
    # Inserting a new entry in the dictionary
    dict[23] = "Jade"
    print(dict)

    '''
    How the output will look like for the above main:

    Key: 1 value: John
    Key: 21 value: Amy
    Key: 2 value: Ann
    Key: 3 value: Jack

    Key: 1 value: Ted
    Key: 21 value: Amy
    Key: 2 value: Ann
    Key: 3 value: Jack

    Key: 21 value: Amy
    Key: 2 value: Ann
    Key: 3 value: Jack

    Key: 21 value: Amy
    Key: 2 value: Ann
    Key: 3 value: Jack
    Key: 23 value: Jade
    '''

if __name__ == "__main__":
    main()
