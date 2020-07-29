
def indexOfmin(lyst):
    minIndex = 0
    currentIndex = 1
    while currentIndex<len(lyst):
         if lyst[currentIndex] < lyst[minIndex]:
                minIndex = currentIndex
         currentIndex+=1
    return minIndex

list = [3,4,86,7,2]

res = indexOfmin(list)
print(res)