# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        transition_flag = False
        result = ListNode()
        current_node = result

        while True:
            if l1:
                current_node.val += l1.val
                l1 = l1.next
            if l2:
                current_node.val += l2.val
                l2 = l2.next
            if transition_flag:
                current_node.val += 1

            transition_flag = True if current_node.val >= 10 else False
            current_node.val = current_node.val % 10

            if not l1 and not l2 and not transition_flag:
                return result
            else:
                current_node.next = ListNode()
                current_node = current_node.next


l1 = ListNode(2,ListNode(4,ListNode(3)))
l2 = ListNode(5,ListNode(6,ListNode(4)))

s = Solution()
result = s.addTwoNumbers(l1,l2)

while result:
    print(result.val, sep = '', end = ',')
    result = result.next
