# coding:utf-8


def shell_sort(li):
    """
    :param li:
    :return:sorted_li
    """
    print "原数组为：", li
    count = len(li)
    step = 3
    group = count / step
    circle = 1
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = li[j]
                while k >= 0 and li[k] > key:
                    li[k + group] = li[k]
                    k -= group
                li[k + group] = key
                j += group
        print "第%d轮排序的结果：" % circle, li
        circle += 1
        group /= step
    return li


if __name__ == '__main__':
    li = [4, 2, 7, 9, 1, 6, 5, 8, 3]
    shell_sort(li)
