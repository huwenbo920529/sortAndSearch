# coding:utf-8


def insert_sort(li):
    """
    直接插入排序:
        将数组分为两部分，有序部分，和无序部分，将无序部分的第一个，不断的插入到有序的部分。
        首先选数组的第一个元素作为有序部分，其余的元素为无序部分。
    :param li: 
    :return: sorted_li
    """
    print "原数组为：", li
    for i in range(1, len(li)):
        key = li[i]
        j = i - 1
        while j >= 0 and li[j] > key:
            li[j + 1] = li[j]
            j -= 1
        li[j+1] = key
        print "第%d轮插入的结果：" % i, li
    return li


if __name__ == '__main__':
    li = [4, 2, 7, 9, 1, 6, 5, 8, 3]
    insert_sort(li)
