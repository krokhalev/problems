# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list2 is None:
            return list1

        while list1:
            box = list2
            run = True

            while run and list1 and box:
                if list1.val < box.val:
                    box.next = ListNode(val=box.val, next=box.next)
                    box.val = list1.val
                    run = False

                if box.next is None:
                    box.next = ListNode(val=list1.val)
                    run = False

                box = box.next

            list1 = list1.next

        return list2


s = Solution()
res = s.mergeTwoLists(
    ListNode(val=2, next=ListNode(val=2, next=ListNode(val=4))),
    ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))
)

while res:
    print(res.val)
    res = res.next
