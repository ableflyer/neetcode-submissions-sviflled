# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        front = fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next
        slow.next = None

        prev = None
        curr = middle
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        middle = prev
        while middle and front:
            front_next = front.next
            front.next = middle

            middle_next = middle.next
            middle.next = front_next

            front = front_next
            middle = middle_next
        
