# coding:utf-8


def select_sort(li):
    """
    1）首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
    2）再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    3）重复第二步，直到所有元素均排序完毕。
    :param li:
    :return: sorted_li
    """
    print "原数组为：", li
    for index in range(len(li) - 1):
        min_index = index
        for i in range(index + 1, len(li)):
            if li[i] < li[min_index]:
                min_index = i
        li[index], li[min_index] = li[min_index], li[index]
        print "第%d轮选择结果：" % (index + 1), li
    return li


if __name__ == '__main__':
    li = [4, 2, 7, 9, 1, 6, 5, 8, 3]
    select_sort(li)
