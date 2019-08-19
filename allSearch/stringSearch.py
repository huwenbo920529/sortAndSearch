# coding:utf-8
charSet = 'ABCDEFG'


# Brute-Force算法简称BF算法:也称简单匹配算法
def naive_match(s, p):
    m, n = len(s), len(p)
    if m-n < 0:
        return -1
    for i in range(m-n+1):
        if s[i:i+n] == p:
            return i
    return -1


# Rabin-Karp算法：
def rabin_karp_match(s, p):
    n = len(s)
    m = len(p)
    h1 = hash(p)
    for i in range(0, n-m+1):
        h2 = hash(s[i:i+m])
        if h1 != h2:
            continue
        else:
            if s[i:i+m] == p:
                return i
    return -1


# KMP算法：
def kmp_match(s, p):
    m, n = len(s), len(p)
    if n == 0 or m - n < 0:
        return -1

    table = partial_table(p)
    i, cur = 0, 0

    while i < m-n+1:
        if p[cur] == s[i+cur]:
            cur += 1
        else:
            if cur == 0:
                i += 1
            else:
                i += cur - table[cur-1]  # 移动位数=已匹配的字符数-对应的部分匹配值
                cur = 0
        if cur == n:
            return i
    return -1


def partial_table(p):
    m = len(p)
    table = [0] * m
    k = 0
    for q in range(1, m):
        if p[k] == p[q]:
            k = k + 1
        else:
            k = 0
            if p[k] == p[q]:
                k = k + 1
        table[q] = k

    return table


# #  根据状态转移函数ơ扫描T匹配字符串：
# def finite_auto_matcher(s, p):
#     m, n = len(s), len(p)
#     print m, n
#     f = compute_transition_function(p, charSet)
#     print f
#     q = 0
#     for i in range(0, m):
#         q = f[(q, s[i])]
#         if q == n:
#             print i+1-n
#             return i+1-n
#     return -1
#
#
# #  构造状态转义函数：
# def compute_transition_function(p, charSet):
#     f = dict()
#     m = len(p)
#     for q in range(0, m):
#         for a in charSet:
#             print a
#             k = min(m, q+1)
#             print "k:", k
#             while not is_post_fix(p[:q]+a, p[:k]):
#                 k -= 1
#                 f[(q, a)] = k
#                 print f
#         print "f:", f
#     for a in charSet:
#         f[(m, a)] = 0
#     print f
#     return f
#
#
# def is_post_fix(s_1, s_2):
#     n = len(s_1)
#     m = len(s_2)
#     for i in range(0, m):
#         if s_1[n-1-i] != s_2[m-1-i]:
#             return False
#         else:
#             return True


# Horspool算法：
def shift_table(p):
    # 生成 Horspool 算法的移动表
    # 当前检测字符为c，模式长度为m
    # 如果当前c不包含在模式的前m-1个字符中，移动模式的长度m
    # 其他情况下移动最右边的的c到模式最后一个字符的距离
    # from collections import defaultdict
    # table = defaultdict(lambda: len(p))
    table = dict()
    # print table
    for index in range(0, len(p) - 1):
        table[p[index]] = len(p) - 1 - index
    # print table
    return table


def horspool_match(s, p):
    m, n = len(s), len(p)
    table = shift_table(p)
    index = len(p) - 1
    while index <= m - 1:
        # print("start matching at", index)
        match_count = 0
        while match_count < n and p[n - 1 - match_count] == s[index - match_count]:
            match_count += 1
        if match_count == len(p):
            return index - match_count + 1
        else:
            # print s[index], table.get(s[index])
            if table.get(s[index]) is None:
                table[s[index]] = n
            index += table[s[index]]
    return -1


# Sunday 算法：
def sunday_match(s, p):
    char_pos = dict()
    for i, ch in enumerate(p):
        char_pos[ch] = i
    # print "char_pos:", char_pos
    i = 0
    m, n = len(s), len(p)
    while i <= m - n:
        found = True
        for j, ch in enumerate(p):
            if s[i + j] != ch:
                found = False
                if (i + n) < m:
                    if s[i + n] not in char_pos:
                        i += (n + 1)
                    else:
                        i += (n - char_pos[s[i + n]])
                else:
                    return -1
                break
        if found:
            return i
    return -1


# Boyer_Moore算法：
def is_character_in(s, c):
    for pos in range(len(s)):
        if s[pos] == c:
            return pos
    return -1
    # try:
    #     pos = s.index(c)
    # except ValueError:
    #     pos = -1
    #
    # return pos


def compare(str1, str2):
    l1 = len(str1) - 1
    l2 = len(str2) - 1

    if l1 != l2:
        return -2, None

    while l1 >= 0:
        if str1[l1] != str2[l1]:
            return l1, str1[l1]
        l1 -= 1

    return 0, None


def boyer_moore_search(string, des):
    l = len(des) - 1
    strlen = len(string) - 1
    start, end = 0, 0
    while strlen >= 0:
        end = start + len(des)
        # print string[start:end]
        cr = compare(string[start:end], des)
        if cr[0] == -2:
            print 'not found'
            break
        if cr[0] == 0:
            # return end - l
            return start
        else:
            pos = is_character_in(des, cr[1])

            if cr[0] == (len(des) - 1):
                if pos != -1:
                    start += len(des) - 1 - pos
                else:
                    start += len(des)
            else:
                if pos == -1:
                    #  have good  string
                    goodPos = is_character_in(des, des[l])
                    if goodPos == l:
                        start += l + 1
                    else:
                        start += l - goodPos


# 快速匹配算法被称为BMHBNFS算法:
def compute_skip(p):
    m = len(p)
    a = p[m-1]
    for i in range(m-2, -1, -1):
        if p[i] == a:
            return m-2-i
    return 0


def python_find(s, p):
    # find first occurrence of p in s
    m = len(s)
    n = len(p)
    # skip是把离p[m-1]最近且字符相同的字符移到m-1位需要跳过的步数-1
    # skip = delta1(p)[p[m - 1]]
    skip = compute_skip(p)
    i = 0
    while i <= m - n:
        if s[i + n - 1] == p[n - 1]:  # (boyer-moore)
            # potential match
            if s[i:i + n - 1] == p[:n - 1]:
                return i
            if s[i + n] not in p:
                i = i + n + 1  # (sunday)
            else:
                i = i + skip  # (horspool)
        else:
            # skip
            if s[i + n] not in p:
                i = i + n + 1  # (sunday)
            else:
                i = i + 1
    return -1  # not found


if __name__ == '__main__':
    s1 = 'ABCDABDABAEEGF'
    p1 = 'BDABAE'
    # print s1.find(p1)
    print "brute_force_match:", naive_match(s1, p1)
    print "kmp_match", kmp_match(s1, p1)
    print "rabin_karp_match:", rabin_karp_match(s1, p1)
    # print finite_auto_matcher(s1, p1)
    print "boyer_moore_search:", boyer_moore_search(s1, p1)
    print "horspool_match:", horspool_match(s1, p1)
    print "sunday_match:", sunday_match(s1, p1)
    print "python_find:", python_find(s1, p1)



