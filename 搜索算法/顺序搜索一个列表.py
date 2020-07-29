def sequentsearch(target, lyst):
    """
    :param target:目标值
    :param lyst: 搜索列表
    :return: 搜素成功返回位置下标  否则返回-1
    """
    position = 0

    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return -1


def binarysearch(target, lystlist):
    start = 0
    end = len(lystlist)

    while start <= end:
        midpoint = (start + end) // 2
        if target == lystlist[min]:
            return midpoint
        elif target > lystlist[min]:
            start = midpoint + 1
        else:
            end = midpoint - 1

    return -1


sortedList = [1, 2, 7, 9, 12]

res = binarysearch(12, sortedList)
print(res)
