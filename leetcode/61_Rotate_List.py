# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: [ListNode], k: int) -> [ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head

        tmp = head
        ll_len = 0
        count_to_return = 0

        while True:
            count_to_return -= 1
            if count_to_return == 1:
                tmp_to_return = head.next
                head.next = None
                return tmp_to_return

            ll_len += 1
            if head.next is None:
                if k == ll_len:
                    return tmp
                elif k > ll_len:
                    count_to_return = ll_len - (k % ll_len) + 1
                else:
                    count_to_return = ll_len - k + 1

                head.next = tmp

            head = head.next


# ll = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None)))))
# k = 17
# ll = ListNode(val=0, next=ListNode(val=1, next=ListNode(val=2, next=None)))
# k = 4
ll = ListNode(val=1, next=ListNode(val=2, next=None))
k = 5
s = Solution()
res_head = s.rotateRight(head=ll, k=k)

while res_head:
    print(res_head.val)
    res_head = res_head.next
