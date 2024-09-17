from collections import deque

class Stack:
    def __init__(self) -> None:
        self.collection = deque()

    def push(self, data: any) -> None:
        self.collection.append(data)

    def pop(self) -> any:
        return self.collection.pop()
    
    def peek(self) -> any:
        return self.collection[-1]
    
    def is_empty(self) -> bool:
        return len(self.collection) == 0
    
    def size(self) -> int:
        return len(self.collection)
    
    def __str__(self) -> str:
        lst = list(self.collection)
        return str(lst)
    
class StrStack(Stack):
    def __init__(self):
        self.string = ''
        super().__init__()

    def reverse_string(self, string: str) -> str:
        for s in string:
            self.push(s)
        for _ in range(len(string)):
            self.string += self.pop()
        return self.string


    

if __name__ == '__main__':
    s = StrStack()

    print(s.reverse_string("We will conquer COVID-19"))
