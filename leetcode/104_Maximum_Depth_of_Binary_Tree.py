class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


s = Solution()
s.maxDepth(TreeNode(val=4, left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)),
                    right=TreeNode(val=7, left=TreeNode(val=6), right=TreeNode(val=9))))
