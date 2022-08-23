class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if (not q or not p) or (p.val != q.val):
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)


s = Solution()
print(s.isSameTree(
    TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3)),
    TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
))
