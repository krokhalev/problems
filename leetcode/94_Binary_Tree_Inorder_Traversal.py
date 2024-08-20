# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        def search(tree):
            if tree:
                return search(tree.left) + [tree.val] + search(tree.right)
            else:
                return []
        return search(root)


n = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3)), right=TreeNode(val=2))
s = Solution()
print(s.inorderTraversal(n))
