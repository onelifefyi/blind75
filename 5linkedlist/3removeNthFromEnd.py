# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Brute:
# First find the length of the LL, then do second pass to remove the nth element

# Approach:
# Have two pointers, right, delayed, and have a variable counter
# Keep moving right (keeping count), when count reaches n + 1, start moving the delayed pointer as well
# Then make delayed -> delayed.next
# Time O(n) | Space O(1)
# def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#     delayed = ListNode()
#     dummy = delayed
#     delayed.next = head
#     right = head
#
#     # giving head start
#     while n > 0 and right:
#         right = right.next
#         n -= 1
#
#     while right:
#         right = right.next
#         delayed = delayed.next
#
#     delayed.next = delayed.next.next
#     # it might be possible that head is removed
#     # return head
#     # so return dummy.next
#     return dummy.next
