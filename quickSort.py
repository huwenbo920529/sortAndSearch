# coding:utf-8

circle = 1


def quick_sort(li, left, right):
    """
    :param li:
    :param left:
    :param right:
    :return: sorted_li
    """
    if left >= right:
        return li
    key = li[left]
    low = left
    high = right
    while left < right:
        while left < right and li[right] >= key:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= key:
            left += 1
        li[right] = li[left]
    li[right] = key
    global circle
    print "第%d轮排序的结果：" % circle, li
    circle += 1
    quick_sort(li, low, left - 1)
    quick_sort(li, left + 1, high)
    return li


if __name__ == '__main__':
    li = [4, 2, 7, 9, 1, 6, 5, 8, 3]
    quick_sort(li, 0, 8)
