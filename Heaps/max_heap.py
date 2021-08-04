class Heap:
     # implementation of binary max heap. Stores arrays as elements with first position corrsponding to the value
    def __init__(self):
        self.heap = []
        self.size = 0

    def getParent(self, index):
        return index // 2

    def getLeftChild(self, parent):
        return 2 * parent

    def getRightChild(self, parent):
        return 2 * parent + 1

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapifyUp(self, index):
        parent = self.getParent(index)

        if self.heap[parent][0] < self.heap[index][0]:
            self.swap(parent, index)
            self.heapifyUp(parent)

    def heapifyDown(self, index):

        leftChild = self.getLeftChild(index)
        rightChild = self.getRightChild(index)

        if leftChild < self.size and self.heap[leftChild][0] > self.heap[index][0]:
            self.swap(leftChild, index)
            self.heapifyDown(leftChild)
        elif rightChild < self.size and self.heap[rightChild][0] > self.heap[index][0]:
            self.swap(rightChild, index)
            self.heapifyDown(rightChild)

    def insert(self, element):

        self.heap.append(element)
        self.size += 1
        self.heapifyUp(self.size - 1)

    def remove(self):
        if self.size == 0:
            return

        self.swap(0, -1)
        element = self.heap.pop()
        self.size -= 1

        if self.heap:
            self.heapifyDown(0)

        return element


if __name__ == "__main__":
    h = Heap()
    h.insert([16, 0])
    h.insert([1, 0])
    h.insert([3, 0])
    h.insert([2, 0])
    h.insert([4, 0])
    h.insert([8, 0])

    print(h.heap)

    print(h.remove())
    print(h.remove())
    print(h.remove())

    print(h.heap)
