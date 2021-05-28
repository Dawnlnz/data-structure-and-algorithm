"""
常用排序算法
1、冒泡排序
2、选择排序
3、插入排序
4、归并排序
5、快速排序
6、堆排序
"""


# 冒泡排序bubble sort
def bubbleSort(arr):
    length = len(arr)
    for i in range(1, length):
        for j in range(0, length-i):
            if arr[j+1] < arr[j]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr

# 选择排序 selection Sort
def selectionSort(arr):
    length = len(arr)
    
    
    for i in range(0,length-1):
        minIndex = i             # 每次检索将有序去第一个元素认为最小
        for j in range(i+1,length):
            # print(j)
            if arr[minIndex] > arr[j]:
                minIndex = j
        if i != minIndex:
            arr[i],arr[minIndex] = arr[minIndex], arr[i]
    return arr

# 插入排序 insertion sort
def insertionSort(arr):
    length = len(arr)
    for i in range(1, length):
        preIndex = i - 1
        current = arr[i]     # 因为元素会后移，会占用当前元素的位置，所以用 current 记录当前需被插入的元素值
        while arr[preIndex] > current and preIndex >= 0:
            arr[preIndex+1] = arr[preIndex]     # 元素后移
            preIndex -= 1
        arr[preIndex + 1] = current     # 将当前元素插入合适的位置
    return arr 

# 希尔排序：shell sort，插入排序的改进
def shellSort(arr):
    length = len(arr)
    gap = 1
    # while(gap > 0):
'''
自顶向下的归并排序
'''
def mergeSortRecursive(S):
    if len(S) < 2:
        return S
    mid = len(S) // 2
    left = S[:mid]
    right = S[mid:]
    # 递归
    left = mergeSortRecursive(left)
    right = mergeSortRecursive(right)
    res = merge(left, right)
    return res

def merge(S1, S2):
    result = []
    i, j = 0, 0
    while len(S1) > 0 and len(S2) > 0:
        if S1[0] < S2[0]:
            # 前后两个数组较小的元素放前面
            result.append(S1.pop(0))
        else:
            result.append(S2.pop(0))
    # 合并剩余数组中的元素，直接添加
    result += S1
    result += S2
    return result

"""
自底向上的归并排序
"""
def merge_0(S, result, start, stride):
    end1 = start + stride
    end2 = min((start + 2*stride), len(S))
    # i:需要合并的子数组1起点
    # j:需要合并的子数组2起点
    # k:需要处理的数组的起点
    i, j, k = start, start + stride, start

    while i < end1 and j < end2:
        if S[i] < S[j]:
            result[k] = S[i]
            i += 1
            k += 1
        else:
            result[k] = S[j]
            j += 1
            k += 1
    # 合并剩余数组
    if i < end1:
        result[k:end2] = S[i:end1]
    if j < end2:
        result[k:end2] = S[j:end2]


def mergeSort(S):
    print()
    L = len(S)
    logn = math.ceil(math.log(L, 2))
    # k 记录第几次合并
    # temp 存储中间排序后的数组
    src, temp = S, [None] * L
    print((2**k for k in range(logn)))
    for stride in (2**k for k in range(logn)):
        for breakpoint in range(0, L, 2*stride):
            # 合并
            merge_0(src, temp, breakpoint, stride)
        # 每排序完一次，将中间结果传递到原结果
        src, temp = temp, src
    return src

def quickSort(S, a, b):
    # base case
    if a >= b:
        return
    left = a
    pivot = S[b]
    right = b-1
    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1
        while left <= right and S[right] > pivot:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left += 1
            right -= 1
    S[left], S[b] = S[b], S[left]
    # 递归左边
    quickSort(S, a, left - 1)
    # 递归右边
    quickSort(S, left + 1, b)
    return S

def heapSort(arr):
    """
    iunput: 无序数组
    """
    # 1、创建大顶堆
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # 循环交换堆顶元素，第一个元素与最后一个元素交换
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
        

def heapify(arr, n, i):
    """
    iunput: 参数1：无序数组arr，参数2：数组元素个数，参数3：需要加入堆的元素索引
    """
    # idx保存根、左、右三者之间较大值的索引
    largest = i
    # 左节点索引(从0开始，所以左节点为i*2+1)
    l = 2 * i + 1    # left = 2 * i + 1
    r = 2 * i + 2    # right = 2 * i + 2
    # 存在左节点，左节点值较大，则取左节点
    if l < n and arr[largest] < arr[l]:
        largest = l
    # 存在右节点，且值较大，取右节点
    if r < n and arr[largest] < arr[r]:
        largest = r
    # 如果根节点较小，则交换值，并继续下沉
    if largest != i:
        # 交换最大元素，将最大元素放到堆顶
        arr[i], arr[largest] = arr[largest], arr[i]
        # 递归构建大顶堆
        heapify(arr, n, largest)

if __name__ == '__main__':
    nums = [5,2,1,4,9,7,6]
    # print(nums)
    res1 = bubbleSort(nums)
    # print(nums)
    res2 = selectionSort([5,2,1,4,9,7,6])
    res3 = insertionSort([5,2,1,4,9,7,6])
    res4 = mergeSortRecursive([5,2,1,4,9,7,6])
    res5 = mergeSort([5,2,1,4,9,7,6])
    res6 = quickSort([5,2,1,4,9,7,6], 0, 6)
    res7 = heapSort([5,2,1,4,9,7,6])
    print(
        "冒泡排序: ",res1,
        "\n选择排序: ", res2,
        "\n选择排序: ", res3,
        "\n归并排序：", res4,
        "\n归并排序：", res5,
        "\n快速排序：", res6,
        "\n堆排序：  ", res7
    )

