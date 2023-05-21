class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


s = Solution()
s.invertTree(TreeNode(val=4, left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)),
                      right=TreeNode(val=7, left=TreeNode(val=6), right=TreeNode(val=9))))
