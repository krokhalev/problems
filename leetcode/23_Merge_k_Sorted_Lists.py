# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None

        first_list = None
        start = None
        for index, ls in enumerate(lists):
            if ls is not None:
                first_list = lists[index]
                start = index
                break

        if first_list is None:
            return None

        for lst in lists[start + 1:]:
            if lst is None:
                continue
            if first_list is None and lst is not None:
                return lst
            while lst:
                ext = False
                ptr = first_list

                while not ext:
                    if lst.val < ptr.val:
                        ptr.next = ListNode(val=ptr.val, next=ptr.next)
                        ptr.val = lst.val
                        ext = True
                    elif ptr.next is None:
                        ptr.next = ListNode(val=lst.val)
                        ext = True
                    ptr = ptr.next

                lst = lst.next

        return first_list


s = Solution()
print(s.mergeKLists(
    [
        ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4))),
        ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4))),
        ListNode(val=3, next=ListNode(val=5, next=ListNode(val=7)))
    ]
))
