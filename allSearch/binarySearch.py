# coding: utf-8


def binary_search(lis, key):
    low = 0
    high = len(lis) - 1
    time = 0
    while low < high:
        time += 1
        mid = int((low + high) / 2)
        if key < lis[mid]:
            high = mid - 1
        elif key > lis[mid]:
            low = mid + 1
        else:
            # 打印折半的次数
            print("times: %s" % time)
            return mid
    print("times: %s" % time)
    return False


def binary_search_recursive(lst, item):
    mid = len(lst) // 2
    found = False
    if lst[mid] == item:
        found = True
        return found
    if mid == 0:
        # mid等于0就是找到最后一个元素了。
        found = False
        return found
    else:
        if item > lst[mid]:  # 找后半部分
            # print(lst[mid:])
            return binary_search_recursive(lst[mid:], item)
        else:
            return binary_search_recursive(lst[:mid], item)  # 找前半部分


if __name__ == '__main__':
    LIST = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = binary_search(LIST, 99)
    print(result)