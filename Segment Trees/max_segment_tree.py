class SegTreeNode:
    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi
        self.val = -float("inf")
        self.lazy = None
        self.children = []
    
class MaxSegTree:
    def __init__(self, lo, hi):
        self.root = SegTreeNode(lo, hi)
    
    def adjustChildren(self, node):
        if node.lo != node.hi:
            if not node.children:
                mid = node.lo + (node.hi - node.lo) // 2
                node.children = [SegTreeNode(node.lo, mid), SegTreeNode(mid + 1, node.hi)]
        
        if node.lazy != None:
            for child in node.children:
                if node.lo != node.hi:
                    child.lazy = node.lazy
                else:
                    child.val = max(child.val, node.lazy)
            
            node.lazy = None
                

    def update(self, i, j, val, node=None):
        node = node or self.root

        if i > node.hi or j < node.lo:
            return 
        
        self.adjustChildren(node)

        if i <= node.lo <= node.hi <= j:
            if val > node.val:
                node.val = val

            if node.lo != node.hi:
                for child in node.children:
                    child.lazy = val
        
            return
        
        for child in node.children:
            self.update(i, j, val, child)
            node.val = max(child.val, node.val)
        
        return
    
    def query(self, i, j, node=None):
        node = node or self.root

        if i > node.hi or j < node.lo:
            return -float("inf")
        
        self.adjustChildren(node)

        if i <= node.lo <= node.hi <= j:
            return node.val
        
        ans = -float("inf")
        for child in node.children:
            ans = max(ans, self.query(i, j, child))
    
        return ans
