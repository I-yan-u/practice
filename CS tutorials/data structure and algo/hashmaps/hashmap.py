class Hashmap:
    def __init__(self):
        self.MAP = 10
        self.arr = [[] for _ in range(self.MAP)]

    def get_hash(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.MAP
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, elements in enumerate(self.arr[h]):
            if len(elements) == 2 and elements[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for elements in self.arr[h]:
            if elements[0] == key:
                return elements[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for elements in self.arr[h]:
            if elements[0] == key:
                del elements

    def __str__(self):
        ret = '{'
        for layer in self.arr:
            for tup in layer:
                ret += f'{tup[0]}: {tup[1]}, '
        ret += '}'
        return ret
            

if __name__ == '__main__':
    t = Hashmap()
    t['march 6'] = 52
    t['march 5'] = 200
    t['march 3'] = 25
    t['march 6'] = 2
    t['march 4'] = 569
    t['march 17'] = 55
    print(t)