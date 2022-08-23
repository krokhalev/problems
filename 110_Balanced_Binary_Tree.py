class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def isBalanced(self, root):
        if not root:
            return True

        self.answer = True

        def count(root):
            left, right = 0, 0

            if root.left:
                left += count(root.left)
            if root.right:
                right += count(root.right)
            if abs(right - left) > 1:
                self.answer = False

            print(root.val, right, left)
            return max(right, left) + 1

        count(root)
        return self.answer


s = Solution()
print(s.isBalanced(TreeNode(val=1,
                            left=TreeNode(val=2, left=TreeNode(val=3, left=TreeNode(val=4), right=TreeNode(val=4)),
                                          right=TreeNode(val=3)), right=TreeNode(val=2))))
