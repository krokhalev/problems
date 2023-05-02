class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        def checkLeft(leftTree):
            if leftTree:
                return [leftTree.val] + checkLeft(leftTree.left) + checkLeft(leftTree.right)
            return [None]

        def checkRight(rightTree):
            if rightTree:
                return [rightTree.val] + checkRight(rightTree.right) + checkRight(rightTree.left)
            return [None]

        return checkLeft(root.left) == checkRight(root.right)


n = TreeNode(val=1, left=TreeNode(val=2, left=None, right=TreeNode(val=3)),
             right=TreeNode(val=2, left=None, right=TreeNode(val=3)))
s = Solution()
print(s.isSymmetric(n))
