class HeapNode:

    def __init__(self, val: int, left: None, right: None):
        self.left = left
        self.right = right
        self.val = val


class Heap:
    def _parentIndex(self, pos):
        return (pos - 1) / 2

    def _leftIndex(self, pos):
        return 2 * pos + 1

    def _rightIndex(self, pos):
        return 2 * pos + 2


class MaxHeap(Heap):
    def __init__(self, l):
        self.length = len(l)
        self.elements = self.build(l)

    def build(self, arr):
        for index in reversed(range(0, int(self.length / 2))):
            self.__heapify(arr, index)
        return arr

    def __heapify(self, arr, i):
        left = self._leftIndex(i)
        right = self._rightIndex(i)
        biggest = i

        if left <= self.length and arr[left] > arr[biggest]:
            biggest = left

        if right <= self.length and arr[right] > arr[biggest]:
            biggest = right

        if biggest != i:
            arr[i], arr[biggest] = arr[biggest], arr[i]
            self.__heapify(arr, biggest)

    def findMax(self):
        return 0

    def insert(self, el):
        return

    def pop(self, el):
        return

    def delete(self):
        return

    def replace(self):
        return


class MinHeap(Heap):
    def __init__(self, l):
        self.l = l

    def __heapify(self, arr, i):
        left = self._leftIndex(i)
        right = self._rightIndex(i)
        smallest = i
        length = (len(arr)) - 1

        if left <= length and arr[i] > arr[left]:
            smallest = left
        if right <= length and arr[smallest] > arr[right]:
            smallest = right
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.__heapify(arr, smallest)


if __name__ == '__main__':
    # 40, 25, 12, 10, 15, 18
    maxHeap = MaxHeap([10, 20, 15, 12, 40, 25, 18])
    minHeap = MinHeap
