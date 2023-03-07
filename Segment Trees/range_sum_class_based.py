class SegTreeNode:
    def __init__(self, lo, hi, val=0):
        self.lo = lo
        self.hi = hi
        self.val = val
        self.lazy = 0
        self.children = []

class SegmentTree:
    def __init__(self, N):
        self.root = SegTreeNode(0, N, 0)
    
    def buildSegTree(self, arr, node=None):
        node = node or self.root
        lo = node.lo
        hi = node.hi

        if lo == hi:
            node.val = arr[lo]
            return 

        mid = lo + (hi - lo) // 2
        
        if not node.children:
            self.formChildren(node)
        
        for child in node.children:
            self.buildSegTree(arr, child)
        
        node.val = sum([child.val for child in node.children])
    
    
    def formChildren(self, node):
        lo = node.lo
        hi = node.hi
        mid = lo + (hi - lo) // 2

        node.children = [SegTreeNode(lo, mid), SegTreeNode(mid + 1, hi)]
        
    def updateSegTree(self, i, j, val, node=None):
        node = node or self.root

        if i > j or i > node.hi or j < node.lo:
            return
        
        if not node.children:
            self.formChildren(node)

        if node.lazy > 0:
            if node.lo != node.hi:
                for child in node.children:
                    child.lazy = node.lazy
            
            node.val += (node.hi - node.lo + 1) * node.lazy
            node.lazy = 0
        
        if i <= node.lo <= node.hi <= j:
            node.val += (node.hi - node.lo + 1) * val
            
            if node.lo != node.hi:
                for child in node.children:
                    child.lazy += val
            
            return
        
        for child in node.children:
            self.updateSegTree(i, j, val, child)

        node.val = sum([child.val for child in node.children])


    def querySegTree(self, i, j, node=None):
        node = node or self.root

        if i > j or i > node.hi or j < node.lo:
            return 0

        if not node.children:
            self.formChildren(node)
        
        if node.lazy > 0:
            if node.lo != node.hi:
                for child in node.children:
                    child.lazy = node.lazy
            
            node.val += (node.hi - node.lo + 1) * node.lazy
            node.lazy = 0
        
        if i <= node.lo <= node.hi <= j:
            return node.val

        return sum([self.querySegTree(i, j, child) for child in node.children])

arr = [1, 2, 3, 4, 5]
N = len(arr)
s = SegmentTree(N - 1)

s.buildSegTree(arr)

print(s.querySegTree(4, 4))
s.updateSegTree(3, 4, 2)
print(s.querySegTree(2, 4))
s.updateSegTree(0, 0, 1)
print(s.querySegTree(0, 4))
s.updateSegTree(0, 2, 3)
print(s.querySegTree(0, 1))

