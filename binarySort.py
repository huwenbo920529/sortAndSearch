# coding: utf-8


def binary_sort(li):
    k = len(li)
    for i in range(1, k):
        left = 0
        right = i - 1
        tmp = li[i]
        while left <= right:
            middle = (right + left) / 2
            if li[middle] < tmp:
                left = middle + 1
            else:
                right = middle - 1
        j = i - 1
        while j >= left:
            li[j + 1] = li[j]
            j -= 1
        li[left] = tmp
        print "第%d轮二分排序的结果：" % i, li
    return li


if __name__ == '__main__':
    li = [4, 2, 7, 9, 1, 6, 5, 8, 3]
    print binary_sort(li)
