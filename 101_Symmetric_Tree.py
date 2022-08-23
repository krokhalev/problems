class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        queue = [root]
        while queue:
            values = []
            for i in queue:
                if i is not None:
                    values.append(i.val)
                else:
                    values.append(None)
            if values != values[::-1]:
                return False

            new_queue = []
            for i in queue:
                if i is not None:
                    for child in (i.left, i.right):
                        new_queue.append(child)
            queue = new_queue

        return True


s = Solution()
print(s.isSymmetric(
    TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3), right=TreeNode(val=4)),
                    right=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=3))),
))
