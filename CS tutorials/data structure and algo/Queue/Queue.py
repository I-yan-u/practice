from collections import deque


class Queue:
    """Implementation of a queue data structure
    """
    def __init__(self) -> None:
        self._buffer = deque()

    def enqueue(self, data: any) -> None:
        """Add data to queue"""
        self._buffer.appendleft(data)

    def dequeue(self) -> any:
        """Removes the first object added to queue"""
        return self._buffer.pop()
    
    def size(self) -> int:
        return len(self._buffer)
    
    def is_empty(self) -> bool:
        return len(self._buffer) == 0
    
    def __str__(self) -> str:
        return f'{self._buffer}'
    

if __name__ == '__main__':
    q = Queue()

    q.enqueue(2)
    q.enqueue(5)
    q.enqueue(235)
    q.enqueue(89)

    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
    
