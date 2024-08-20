# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        res = ListNode()
        tail = res

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return res.next


s = Solution()
output = s.mergeTwoLists(
    ListNode(val=2, next=ListNode(val=2, next=ListNode(val=4))),
    ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))
)

while output:
    print(output.val)
    output = output.next
