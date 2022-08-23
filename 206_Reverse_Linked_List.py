# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        reverse_arr = arr
        reverse_arr.reverse()

        root = None
        for elem in reverse_arr:
            box = ListNode(val=elem)

            if root is None:
                root = box
            else:
                prt = root
                while prt.next is not None:
                    prt = prt.next
                prt.next = box
        return root


s = Solution()
print(s.reverseList(ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None)))))))