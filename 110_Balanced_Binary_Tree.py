class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        def height(node: TreeNode):
            if not node:
                return 0, True
            left_height, balanced = height(node.left)
            if not balanced:
                return left_height, False
            right_height, balanced = height(node.right)
            if not balanced:
                return right_height, False

            return max(left_height, right_height) + 1, abs(left_height - right_height) < 2

        _, balanced = height(root)
        return balanced


s = Solution()
print(s.isBalanced(TreeNode(1, TreeNode(1), TreeNode(1, TreeNode(1)))))
