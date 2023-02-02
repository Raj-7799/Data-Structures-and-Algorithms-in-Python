class SegmentTree:
    def __init__(self, N):
        self.tree = 4 * N * [0]
        self.lazy = 4 * N * [0]
    
    def buildSegTree(self, arr, treeIdx, lo, hi):
        if lo == hi:
            self.tree[treeIdx] = arr[lo]
            return
        
        mid = lo + (hi - lo) // 2

        left = 2 * treeIdx + 1
        right = 2 * treeIdx + 2

        self.buildSegTree(arr, left, lo, mid)
        self.buildSegTree(arr, right, mid + 1, hi)

        self.tree[treeIdx] = self.tree[left] + self.tree[right]
    
    def updateLazySegTree(self, treeIdx, lo, hi, i, j, val):
        if lo > hi or i > hi or  j < lo:
            return
        
        left = 2 * treeIdx + 1
        right = 2 * treeIdx + 2

        if self.lazy[treeIdx] != 0:
            self.tree[treeIdx] += (hi - lo + 1) * self.lazy[treeIdx]

            if lo != hi:
                self.lazy[left] += self.lazy[treeIdx]
                self.lazy[right] += self.lazy[treeIdx]

            self.lazy[treeIdx] = 0
        
        if i <= lo <= hi <= j:
            self.tree[treeIdx] += (hi - lo + 1) * val

            if lo != hi:
                self.lazy[left] += val
                self.lazy[right] += val
            
            return

        mid = lo + (hi - lo) // 2
        self.updateLazySegTree(left, lo, mid, i, j, val)
        self.updateLazySegTree(right, mid + 1, hi, i, j, val)
        self.tree[treeIdx] = self.tree[left] + self.tree[right]
    
    def queryLazySegTree(self, treeIdx, lo, hi, i, j):
        if lo > hi or i > hi or  j < lo:
            return 0
        
        left = 2 * treeIdx + 1
        right = 2 * treeIdx + 2

        if self.lazy[treeIdx] != 0:
            self.tree[treeIdx] += (hi - lo + 1) * self.lazy[treeIdx]
            if lo != hi:
                self.lazy[left] += self.lazy[treeIdx]
                self.lazy[right] += self.lazy[treeIdx]

            self.lazy[treeIdx] = 0
        
        if i <= lo <= hi <= j:
            return self.tree[treeIdx]
        
        mid = lo + (hi - lo) // 2

        leftQ = self.queryLazySegTree(left, lo, mid, i, j)
        rightQ = self.queryLazySegTree(right, mid + 1, hi, i, j)

        return leftQ + rightQ

arr = [1, 2, 3, 4, 5]
N = len(arr)
s = SegmentTree(N)

s.buildSegTree(arr, 0, 0, N - 1)

print(s.queryLazySegTree(0, 0, N - 1, 4, 4))
s.updateLazySegTree(0, 0, N - 1, 3, 4, 2)
print(s.queryLazySegTree(0, 0, N - 1, 2, 4))
s.updateLazySegTree(0, 0, N - 1, 0, 0, 1)
print(s.queryLazySegTree(0, 0, N - 1, 0, 4))
s.updateLazySegTree(0, 0, N - 1, 0, 2, 3)
print(s.queryLazySegTree(0, 0, N - 1, 0, 1))

