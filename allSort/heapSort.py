# coding:utf-8


def adjust_heap(li, i, size):
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    max_ = i
    if i < size / 2:
        if left_child < size and li[left_child] > li[max_]:
            max_ = left_child
        if right_child < size and li[right_child] > li[max_]:
            max_ = right_child
        if max_ != i:
            li[max_], li[i] = li[i], li[max_]
            adjust_heap(li, max_, size)


def build_heap(li, size):
    for i in range(0, (size / 2))[::-1]:
        adjust_heap(li, i, size)
    print '循环建立初始堆后的结果为：',li

def heap_sort(li):
    size = len(li)
    build_heap(li, size)
    for i in range(0, size)[::-1]:
        li[0], li[i] = li[i], li[0]
        adjust_heap(li, 0, i)
        print "第{}次交换后的结果为：{}".format(size-i,li)
    return li

if __name__ == '__main__':
    li = [4, 2, 7, 9, 1, 6, 5, 8, 3]
    heap_sort(li)
