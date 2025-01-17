import random

class Sort:
    def __init__(self, n):
        self.len = n
        self.arr = [0] * n
        self.random_data()

    def random_data(self):
        # 生成随机数
        for i in range(self.len):
            self.arr[i] = random.randint(0, 100)

    def partition(self, left, right):
        pivot = self.arr[left]  # 选择第一个元素作为基准值
        while left < right:
            # 从右向左找第一个小于基准值的元素
            while left < right and self.arr[right] >= pivot:
                right -= 1
            self.arr[left] = self.arr[right]  # 将小于基准值的元素放到左边

            # 从左向右找第一个大于基准值的元素
            while left < right and self.arr[left] <= pivot:
                left += 1
            self.arr[right] = self.arr[left]  # 将大于基准值的元素放到右边

        self.arr[left] = pivot  # 将基准值放到正确的位置
        return left  # 返回基准值的位置

    def quick_sort(self, left, right):
        if left < right:
            pivot = self.partition(left, right)  # 获取基准值的位置
            self.quick_sort(left, pivot - 1)  # 递归排序左半部分
            self.quick_sort(pivot + 1, right)  # 递归排序右半部分

    def adjust_max_heap(self, pos, arr_len):
        dad = pos
        son = 2 * dad + 1
        while son < arr_len:
            if son + 1 < arr_len and self.arr[son] < self.arr[son + 1]:
                son += 1  # 选择较大的子节点
            if self.arr[son] > self.arr[dad]:
                self.arr[dad], self.arr[son] = self.arr[son], self.arr[dad]  # 交换父子节点
                dad = son
                son = 2 * dad + 1
            else:
                break

    def heap_sort(self):
        # 构建最大堆
        for i in range(self.len // 2 - 1, -1, -1):
            self.adjust_max_heap(i, self.len)

        # 逐个交换堆顶元素和最后一个元素，并调整堆
        for i in range(self.len - 1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]  # 交换堆顶和最后一个元素
            self.adjust_max_heap(0, i)  # 调整堆

if __name__ == '__main__':
    my_sort = Sort(10)
    print("原始数组:", my_sort.arr)

    # 快速排序
    my_sort.quick_sort(0, my_sort.len - 1)
    print("快速排序后数组:", my_sort.arr)

    # 重新生成随机数组
    my_sort.random_data()
    print("重新生成的数组:", my_sort.arr)

    # 堆排序
    my_sort.heap_sort()
    print("堆排序后数组:", my_sort.arr)