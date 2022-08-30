# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list2 is None:
            return list1

        while list1:
            ext = False
            ptr = list2

            while not ext:
                if list1.val < ptr.val:
                    ptr.next = ListNode(val=ptr.val, next=ptr.next)
                    ptr.val = list1.val
                    ext = True
                elif ptr.next is None:
                    ptr.next = ListNode(val=list1.val)
                    ext = True
                ptr = ptr.next

            list1 = list1.next

        return list2


s = Solution()
print(s.mergeTwoLists(
    ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4))),
    ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))
))
