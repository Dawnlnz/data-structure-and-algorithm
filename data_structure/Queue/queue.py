'''基于列表实现队列'''
class Queue(object):
    # 默认队列空间大小为10
    DEFAULT_CAPACITY = 10
    def __init__(self):
        """创建一个空的队列"""
        self._queue = [None] * Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def length(self):
        """返回队列的大小"""
        return self._size

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.length() == 0

    def enqueue(self, elem):
        """往队列中添加一个item元素"""
        if self._size == len(self._queue):
            self._resize(2 * len(self._queue))
        avail = (self._front + self._size) % len(self._queue)
        self._queue[avail] = elem
        self._size += 1
    def _resize(self, cap):
        '''resize to a new list of capacity >= len(self)'''
        old = self._queue
        self._queue = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._queue[k] = old[walk]
            walk = (1+walk) % len(old)   # 遍历原数组进行赋值
        self._front = 0


    def dequeue(self):
        """从队列头部删除一个元素"""
        if self.is_empty():
            raise QueueError("The stack is empty.")
        else:
            res = self._queue[self._front]
            self._queue[self._front] = None
            self._front = (self._front + 1) % len(self._queue)
            self._size -= 1
            return res  

    def first(self):
        if self.is_empty():
            raise QueueError("The stack is empty.")
        return self._queue[self._front]


'''基于链表实现队列'''
class LNode(object):
    def __init__(self, item, next_ = None):
        self.item = item
        self.next = next_
    


class LQueue(object):
    def __init__(self):
        # 队首
        self._head = None
        # 队尾
        self._rear = None

    def is_empty(self):
        return self._head is None
    
    def length(self):
        count = 0
        cur = self._head
        while cur.next is not None:
            count += 1
            cur = cur.next
        return count

    def peek(self):
        if self.is_empty():
            raise QueueError("The stack is empty.")
        return self._head.item
    
    def enqueue(self, item):
        '''尾插法'''
        elem = LNode(item)
        if self.is_empty():
            self._head = elem
            self._rear = elem
        else:
            self._rear.next = elem
            self._rear = elem

    def dequeue(self):
        if self.is_empty():
            raise QueueError("The stack is empty.")
        res = self._head.item
        self._head = self._head.next
        return res


def main():
    queue = Queue()
    print(queue.is_empty())
    for i in range(13):
        queue.enqueue(i)
    print("the head = ", queue.first())
    print("lqueue.length = ", queue.length())
    print(queue.is_empty())
    while queue.length() > 0:
        print(queue.dequeue())
        print("queue.length = ", queue.length())
    print(queue.is_empty())

    lqueue = LQueue()
    print(lqueue.is_empty())
    for i in range(6):
        lqueue.enqueue(i)
    print("the head = ", lqueue.peek())
    print("lqueue.length = ", lqueue.length())
    print(lqueue.is_empty())
    while lqueue.length() > 0:
        print(lqueue.dequeue())
        print("lqueue.length = ", lqueue.length())
    print(lqueue.is_empty())

if __name__ == '__main__':
    main()
    
