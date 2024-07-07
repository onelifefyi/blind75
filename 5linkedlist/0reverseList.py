# https://leetcode.com/problems/reverse-linked-list/
# Check Leetcode link for execution

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach:
# If head is none, return head
# Set curr to head and prev to none
# iterate while curr exists, store curr.next in tmp variable
# set curr.next to tmp
# set prev to curr
# set curr to tmp
# after the loop ends, finally set the head to prev
# Time O(n) | Space O(1)

# def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#     if not head: return head
#     curr = head
#     prev = None
#     while curr:
#         tmp = curr.next
#         curr.next = prev
#         prev = curr
#         curr = tmp
#     head = prev
#     return head
