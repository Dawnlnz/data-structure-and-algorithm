# python 数据结构之队列

## 一、队列简介

队列（queue）是只允许在一端进行插入操作，而在另一端进行删除操作的线性表。
队列是一种先进先出的（FIFO，First In First Out）的线性表，允许插入的一端为队尾，允许删除的一端为队头。队列数据结构的操作和我们平时排队是一致的，排在队头的先出列完成事务，新来的人只能排在队尾。

<img src="E:\algorithm\data_structure\队列.png" alt="队列"  />

## 二、队列的实现

队列的常用操作为：

- Queue() 创建一个空的队列
- enqueue(elem) 往队列中添加一个elem元素
- dequeue() 从队列头部删除一个元素
- is_empty() 判断一个队列是否为空
- length() 返回队列的大小

```python
class Queue(object):
    def __init__(self):
        """创建一个空的队列"""
        self.queue = []
    
    def length(self):
        """返回队列的大小"""
        return len(self.queue)

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.length() == 0

    def enqueue(self, elem):
        """往队列中添加一个item元素"""
        self.queue.append(elem)

    def dequeue(self):
        """从队列头部删除一个元素"""
        if self.is_empty():
            return None
        else:
            return self.queue.pop()
```

示例：操作队列

```python
def main():
    queue = Queue()
    print(queue.is_empty())
    for i in range(5):
        queue.enqueue(i)
    print(queue.is_empty())
    print(queue.dequeue())
    print(queue)

if __name__ == '__main__':
    main()
```

## 三、双向队列

deque模块是Python标准库collections中的一个内置模块，实现双端队列的功能，在队列的两端都可以进行插入和删除。

使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为`list`是线性存储，数据量大的时候，插入和删除效率很低。

deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

deque的种基本操作：

- append(item)： 入队，从队列右端插入一个元素
- appendleft(item)： 入队，从队列左端删除一个元素
- extend(item)： 迭代处理其输入，对每个元素完成与append()相同的处理
- extendleft(item)： 迭代处理其输入，对每个元素完成与appendleft()相同的处理
- pop()： 出队，从队列右端删除一个元素，并返回该元素
- popleft()： 出队，从队列左端删除一个元素，并返回该元素
- rotate(index)：将队列的某些元素按某一方向进行旋转。参数为正数n时，将右端的n个元素依次插入到左端；参数为负数n时，将左端的n个元素依次插入到右端

