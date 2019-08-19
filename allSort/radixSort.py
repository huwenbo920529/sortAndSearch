# coding: utf-8
import math


def radix_sort(lists, radix=5):
    k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in lists:
            print j/(radix**(i-1)) % (radix**i)
            bucket[j/(radix**(i-1)) % (radix**i)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists


if __name__ == '__main__':
    li = [4, 2, 7, 9, 1, 6, 5, 8, 3]
    print radix_sort(li)