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
        new_arr = []
        for lst in lists:
            while lst:
                new_arr.append(lst.val)
                lst = lst.next

        new_arr = sorted(new_arr)

        root = None
        for elem in new_arr:
            temp = ListNode(val=elem)

            if root is None:
                root = temp
            else:
                ptr = root
                while ptr.next is not None:
                    ptr = ptr.next
                ptr.next = temp

        return root



