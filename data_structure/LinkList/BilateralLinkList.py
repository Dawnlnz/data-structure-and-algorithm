class Node(object):
    '''双向链表节点'''
    def __init__(self, item):
        # item 存放数据元素
        self.item = item
        # next 指向下一节点的地址
        self.next = None
        # prev 指向上一节点的地址
        self.prev = None

class BilateraLinkList(object):
    '''双向链表'''
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
        # 链表非空
        count = 0
        cur = self._head
        while cur.next is not None:
            count += 1
            # 指针后移
            cur = cur.next
        return count
    
    def items(self):
        '''遍历链表'''
        # 获取头指针
        cur = self._head
        # 循环遍历链表
        while cur.next is not None:
            # 返回生成器
            yield cur.item
            # 指针下移
            cur = cur.next
    
    def add(self, item):
        '''向链表头部添加元素'''
        node = Node(item)
        # 链表为空
        if self.is_empty:
            # 头部节点指针修改为新节点
            self._head = node
        # 链表非空
        else:
            # 新节点指针指向原头部指针
            node.next = self._head
            # 原头部节点 prev 指向新节点
            self._head.prev = node
            # 修改 head 指向新节点
            self._head = node

    def append(self, item):
        '''链表尾部添加元素'''
        node = Node(item)
        # 链表为空
        if self.is_empty():
            self._head = node
        # 链表非空
        else:
            cur = self._head
            # 循环移动到尾部节点
            while cur.next is not None:
                cur = cur.next
            # 新节点上一级指针指向旧尾部
            node.prev = cur
            # 旧链表尾部指向新节点
            cur.next = node
            
    def insert(self, index, item):
        '''链表指定位置插入元素'''
        # 指定插入位置位于链表头部
        if index <= 0:
            self.add(item)
        # 指定插入位置位于链表尾部
        elif index > self.length()-1:
            self.append(item)
        # 指定位置位于链表之中
        else:
            cur = self._head
            node = Node(item)
            for i in range(index):
                cur = cur.next
            # 新节点的向下指针指向当前节点
            node.next = cur
            # 新节点的向上指针指向当前节点的上一节点
            node.prev = cur.prev
            # 当前节点的上一节点的向下指向新节点
            cur.prev.next = node
            # 当前节点的向上指针指向新节点
            cur.prev = node
    
    def remove(self, item):
        '''删除指定元素的第一个节点'''
        # 链表为空
        if self.is_empty():
            return
        # 链表非空
        cur = self._head
        if cur.item == item:
            # 删除节点为头节点
            if cur.next is None:
                # 链表只有一个元素
                self._head = None
                return True
            else:
                # head 指向下一节点
                self._head = cur.next
                # 下一节点的向上指针指向None
                cur.next.prev = None
                return True
        while cur.next is not None:
            # 删除节点非头点：遍历链表，直到找到需要删除的元素
            if cur.item == item:
                # 上一节点的next指向当前节点的下一节点
                cur.prev.next = cur.next
                # 下一节点的prev指向当前节点的上一节点
                cur.next.prev = cur.prev
                return True
            cur = cur.next
        # 删除节点为尾节点
        if cur.item == item:
            cur.prev.next = None
            return True
    
    def find(self, item):
        return item in self.items()

def main():
    linkList = BilateraLinkList()
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

        
            

            
            