# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @classmethod
    def node_to_array(cls, node):
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        return arr

    @classmethod
    def sum_numbers(cls, arr):
        number = ""
        for elem in arr:
            number += str(elem)

        return int(number)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first_array = self.node_to_array(l1)
        second_array = self.node_to_array(l2)

        first_array.reverse()
        second_array.reverse()

        first_arr_sum = self.sum_numbers(first_array)
        second_arr_sum = self.sum_numbers(second_array)
        sum_numbers_to_arr = list(str(first_arr_sum + second_arr_sum))
        sum_reverse = sum_numbers_to_arr
        sum_reverse.reverse()

        root = None
        for elem in sum_reverse:
            temp = ListNode(val=int(elem))

            if root is None:
                root = temp
            else:
                prt = root
                while prt.next is not None:
                    prt = prt.next
                prt.next = temp

        return root


l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))
s = Solution()
print(s.addTwoNumbers(l1, l2))
