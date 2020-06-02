def mergeRec(array, left, right):
    left_length = len(left)
    right_lengt = len(right)
    i = 0
    j = 0
    k = 0
    while i < left_length and j < right_lengt:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < left_length:
        array[k] = left[i]
        i += 1
        k += 1

    while j < right_lengt:
        array[k] = right[j]
        j += 1
        k += 1


def mergeSort(array):
    if (len(array) < 2):
        return
    mid = int(len(array) / 2)
    left = array[:mid]
    right = array[mid:]

    mergeSort(left)
    mergeSort(right)

    return mergeRec(array, left, right)


def quickSort(array):
    return quickSortRec(array, 0, len(array) - 1)


def quickSortRec(array, start, end):
    if start < end:
        partitionIndex = partition(array, start, end)
        quickSortRec(array, start, partitionIndex - 1)
        quickSortRec(array, partitionIndex + 1, end)
    return array


def swap(array, pos1, pos2):
    array[pos1], array[pos2] = array[pos2], array[pos1]


def partition(array, start, end):
    pivot = array[end]
    partion_index = start
    counter = 0
    for i in range(start, end):
        if array[i] <= pivot:
            swap(array, i, partion_index)
            counter += 1
            print("swap number {}".format(counter))
            partion_index += 1

    swap(array, partion_index, end)
    return partion_index



def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selectionSort(arr):
    n = len(arr)

    for i in range(len(arr)):

        min_idx = i
        for j in range(i + 1, len(arr)):
            if (arr[min_idx] > arr[j]):
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def minimumSwaps2(arr):
    sortedPositions = {}
    for idx, el in enumerate(arr):
        sortedPositions[el] = idx

    counter = 0
    for idx, el in enumerate(arr):
        # we need to swap
        if el is not idx + 1:
            curPosOfExpected = sortedPositions[idx + 1]
            arr[idx], arr[curPosOfExpected] = idx + 1, el

            sortedPositions[el], sortedPositions[idx + 1] = sortedPositions[idx + 1], idx
            counter += 1
    return counter


def minimumSwaps(arr):
    temp = {a: i for i, a in enumerate(arr)}
    swaps = 0
    for i in range(len(arr)):
        actual, expected = arr[i], i + 1
        arr.__getitem__()
        actual_i, expected_i = i, temp[expected]
        if actual != expected:
            arr[actual_i] = expected
            arr[expected_i] = actual
            temp[actual] = expected_i
            temp[expected] = actual_i
            swaps += 1
    return swaps


if __name__ == "__main__":
    # k = [1, 35, 6, 2, 62, 62, 34, 4]
    # k = [7, 2, 1, 6, 8, 5, 3, 4]
    k = [4, 3, 1,2]
    # k = [12, 11, 13, 5, 6]
    # print(mergeSort(array=k))
    # print(insertionSort(arr=k))
    # print(selectionSort(arr=k))
    print(minimumSwaps(arr=k))
