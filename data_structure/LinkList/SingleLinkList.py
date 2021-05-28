class Node(object):
    '''单向链表的节点'''
    def __init__(self, item):
        # item 存放数据元素
        self.item = item
        # next 是下一个节点的地址
        self.next = None

class SingleLinkList(object):
    '''单向链表'''
    def __init__(self):
        self._head = None

    def is_empty(self):
        '''判断链表是否为空'''
        return self._head is None
    
    def length(self):
        '''链表长度'''
        # 初始指针指向head
        cur = self._head
        count = 0
        # 指针指向None 表示到达尾部
        while cur is not None:
            count += 1
            # 指针后移
            cur = cur.next
        return count
    
    def items(self):
        '''遍历链表'''
        # 获取head 指针
        cur = self._head
        # 遍历循环
        while cur is not None:
            # 返回生成器
            yield cur.item
        cur = cur.next
	
    def add(self, item):
        '''向链表头部添加元素'''
        node = Node(item)
        # 将新节点指针指向原头部节点
        node.next = self._head
        # 头部节点指针修改为新节点
        self._head = node
        
    def append(self, item):
        '''向链表尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            # 空链表, _head 指向新节点
            self._head = node
        else:
            # 非空链表，则找到尾部， 将尾部next 节点指向新节点
            cur = self._head
            if cur.next is not None:
                cur = cur.next
            else:
                cur.next = node
                
    def insert(self, index, item):
        '''在单链表指定位置插入元素'''
        # 指定位置在第一个元素之前，在头部插入
        if index <= 0:
            self.add(item)
        # 指定位置超过尾部，在尾部插入
        elif index >= (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            # 循环到需要插入的位置
           	for i in range(index-1):
                cur = cur.next
            node.next = cur.next
            cur.next = node
            
    def remove(self, item):
        '''删除节点'''
        cur = self.item
        pre = None
        while cur is not None:
            # 找到指定元素
            if cur.item == item:
                # 如果第一个元素就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前的一个节点的next指向删除元素的后一个节点
                    pre.next = cur.next
                return True
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next
    def find(self, item):
        '''查找元素是否存在'''
        return item in self.items()
def main():
    # 创建链表
    linkList = SingleLinkList()
    # # 创建节点
    # node1 = Node(1)
    # node2 = Node(2)

    # # 将节点添加到链表
    # linkList._head = node1
    # # 将第一个节点的next指针指向下一个节点
    # node1.next = node2

    # # 访问链表
    # print(linkList._head.item)   # 访问第一个节点数据
    # print(linkList._head.next.item) # 访问第二个节点数据

     # 向链表尾部添加数据
    for i in range(5):
        linkList.append(i)
    # 向链表头部添加数据
    linkList.add(6)
    # 遍历链表数据
    for i in linkList.items():
        print(i,end='\t')
    # 链表指定位置插入元素
    linkList.insert(3,9)
    print('\n', linkList.items())
    # 删除链表数据集
    linkList.remove(0)
    # 查找链表数据
    print(linkList.find(4))

if __name__ == "__main__":
    main()
   