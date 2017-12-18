# Case : len 5 (0-4) l=0,m=2 r =4 3
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]


def merge(array, left, mid, right):
    countConversion = 0
    countL = mid - left + 1
    countR = right - mid
    lArray = [None] * countL
    rArray = [None] * countR

    for i in range(countL):  # count of elements l to m(inclusive)
        lArray[i] = array[left + i]
    for i in range(countR):  # count of elements m+1 to r(inclusive)
        rArray[i] = array[mid + i + 1]

    # Merging the subArrays
    j = 0
    i = 0
    k = left  # Index of merged subarray

    while i < countL and j < countR:
        if lArray[i] <= rArray[j]:
            array[k] = lArray[i]
            i += 1
            countConversion += 1
        else:
            array[k] = rArray[j]
            j += 1
            countConversion += 1
        k += 1
    while i < countL:
        array[k] = lArray[i]
        i += 1
        k += 1
        # countConversion+=1
    while j < countR:
        array[k] = rArray[j]
        j += 1
        k += 1
        # countConversion+=1
    # print('countConversion', countConversion)
    return countConversion


def __sort(array, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2
        __sort(array, left, mid)
        __sort(array, mid + 1, right)
        count = merge(array, left, mid, right)
    return count


def sort(array):
    count = __sort(array, 0, len(array) - 1)
    return count


# Main method
def Main():
    arry = [2, 1, 3, 1, 2]
    print(arry)
    count = sort(arry)
    # print('count', count)
    print(count)


Main()
