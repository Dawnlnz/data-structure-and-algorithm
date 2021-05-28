class Node(object):
    '''循环链表节点'''

    def __init__(self, item):
        # item 存放数据元素
        self.item = item
        # next 是下一个节点的地址
        self.next = None

class SingleCycleLinkList(object):
    def __init__(self):
        self._head = None
    
    def is_empty(self):
        '''判断链表是否为空'''
        return self._head is None

    def length(self):
        '''获取链表长度'''
        # 链表为空
        if self.is_empty():
            return 0
        count = 0
        cur = self._head
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count
    
    def items(self):
        '''遍历链表'''
        # 链表为空
        if self.is_empty():
            return
        # 链表不为空
        cur = self._head
        while cur.next != self._head:
            yield cur.item
            cur = cur.next
        yield cur.item
    
    def add(self, item):
        '''链表头部添加节点'''
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            # 添加节点指向head
            node.next = self._head
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
        # 修改 head 指向新节点
        self._head = node
    def append(self, item):
        # 向尾部添加元素
        node = Node(item)
        # 链表为空
        if self.is_empty():
            self._head = node
            self.next = self._head
        # 链表非空
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            # 新节点指针指向head
            node.next = self._head
    
    def insert(self, index, item):
        # 指定位置小于等于0，在链表头部添加
        if index <= 0:
            self.add(item)
        # 指定位置大于链表长度，在链表尾部添加
        elif index > self.length()-1:
            self.append(item)
        else:
            cur = self._head
            node = Node(item)
            for i in range(index - 1):
                cur = cur.next
            # 新节点指针指向旧节点
            node.next = cur.next
            # 旧节点指针指向新节点
            cur.next = node
    
    def remove(self, item):
        '''删除数据值为item的节点'''
        if self.is_empty():
            return
        cur = self._head
        pre = Node
        # 链表第一个元素为需要删除的元素
        if cur.item == item:
            # 链表不止一个元素
            if cur.next != self._head:
                while cur.next != self._head:
                    cur = cur.next
                # 尾节点指向头部节点的下一个节点
                cur.next = self._head.next
                # 删除头部节点，调整头部节点为头节点下一节点
                self._head = self._head.next
            else:
                # 只有一个元素
                self._head = None
        else:
            # 不是第一个元素
            pre = self._head
            # 遍历链表查找元素
            while cur.next != self._head:
                if cur.item == item:
                    # 删除元素
                    pre.next = cur.next
                    return True
                else:
                    # 记录前一个指针
                    pre = cur   
                    #调整指针位置
                    cur = cur.next
        # 删除元素在末尾
        if cur.item == item:
            pre.next = self._head
            return True
    
    def find(self, item):
        '''查找元素'''
        return item in self.items()
    

def main():
    linkList = SingleCycleLinkList()
    print(linkList.is_empty())
    # 头部添加元素
    for i in range(5):
        linkList.add(i)
    print(list(linkList.items()))
    # 尾部添加元素
    for i in range(6):
            linkList.append(i)
    print(list(linkList.items()))
    # 添加元素
    linkList.insert(3, 45)
    print(list(linkList.items()))
    # 删除元素
    linkList.remove(5)
    print(list(linkList.items()))
    # 元素是否存在
    print(linkList.find(4))

if __name__ == '__main__':
    main()

            

        