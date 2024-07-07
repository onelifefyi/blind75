# https://leetcode.com/problems/reorder-list/description/

# Brute:
# Create a copy of the linked list, reverse it (track length)
# Create another linked list, in that keep inserting first from original list, then from second list till length
# Time O(n) | Space O(n)

# Approach:
# Two pointers slow and fast to find the mid point
# Reverse the list after mid (using new variable)
# Then start from the start, after first, insert from the reversed side & keep going till you reach the mid
# set the last.next to Null

# def reorderList(self, head: Optional[ListNode]) -> None:
#     """
#     Do not return anything, modify head in-place instead.
#     """
#     slow, fast = head, head
#     while fast.next and fast.next.next:
#         slow = slow.next
#         fast = fast.next.next
#
#     mid = slow
#     prev = None
#     while slow:
#         tmp = slow.next
#         slow.next = prev
#         prev = slow
#         slow = tmp
#     reversedHead = prev
#
#     mid.next = None
#     # Now we have two linkedlists | one starting at head
#     # The other starting at reversedHead
#     # Now, alternatively merge
#
#     headBkp = head
#     while head and reversedHead:
#         tmp = head.next
#         head.next = reversedHead
#         revTmp = reversedHead.next
#         reversedHead.next = tmp
#         head = tmp
#         reversedHead = revTmp
#     if head:
#         reversedHead = head
#     elif reversedHead:
#         head = reversedHead
#
#     return headBkp
