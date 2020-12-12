class SLDictionary:
    def __init__(self, filename):
        self.arr = self.dictionary_file(filename)
        self._size = len(self.arr)
        self._quick_sort(self.arr, 0, self._size-1)
        self._dict_list = self.arr

    @classmethod
    def dictionary_file(cls, filename):
        file1 = open(filename, 'r')
        count = 0
        list = []
        for line in file1:
            count += 1
            list.append(eval(line))
        file1.close()
        return list

    def save_dictionary(self, filename):
        with open(filename, 'w') as filehandle:
            for listitem in self._dict_list:
                filehandle.write('%s\n' % listitem)

    def _insertion_sort(self, arr):
        for i in range(1, self._size):
            key = arr[i]
            j=i-1
            while j>=0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

    def _quick_sort(self, arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = self.partition(arr, low, high)
            self._quick_sort(arr, low, pi-1)
            self._quick_sort(arr, pi+1, high)

    def partition(self, arr, low, high):
        i = (low-1)
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    #adopted from lldict
    def __len__(self):
        return self._size

    #adopted from lldict
    def __contains__(self, key):
        return not self._find(key) is -1

    def _find(self, key):
        for i, j in enumerate(self._dict_list):
            if j[0] == key:
                return i
        return -1

    def __getitem__(self, key):
        item = self._find(key)
        if item == -1:
            raise KeyError("Item does not exist")
        return self._dict_list[item]

    def __setitem__(self, key, value):
        self._insert(key, value)

    def _insert(self, key, value):
        item = self._find(key)
        if item == -1:
            #if key doesn't exist in array yet, insert the item and sort
            self._dict_list.append([key, value])
            self._insertion_sort(self._dict_list)
        else:
            #if key is found, change the item found
            self._dict_list[item] = [key, value]

    def pop(self, key):
        item = self._find(key)
        if item == -1:
            #if key doesn't exist, raise an error
            raise KeyError("Item does not exist")
        else:
            self._dict_list.pop(item)

    def __str__(self):
        end = ""
        for i in self._dict_list:
             end += (str(i) + ", ")
        return(end)

def main():
    dict = SLDictionary('slstartlist.txt')
    results = dict[1]
    print("Results of getting item at index 1: " + str(results))
    dict[1] = "Test"
    results = dict[1]
    print("Results of getting item at index 1 after changing it to \"Test\": " + str(results))
    print("Results of the entire dict after this operation: " + str(dict))
    dict.pop(1)
    print("Results of the entire dict after popping item at index 1: " + str(dict))
    dict[len(dict) + 3] = "Last"
    results = dict[len(dict) + 3]
    print("Results of getting item at the index of 3 after the previous length after setting it to \"Last\":  " + str(results))
    print("Results of the entire dict after this operation: " + str(dict))
    dict.save_dictionary("slendlist.txt")

if __name__ == "__main__":
    main()
