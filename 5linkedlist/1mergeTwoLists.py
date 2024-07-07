# https://leetcode.com/problems/merge-two-sorted-lists/
# Check Leetcode link for execution

# Approach:
# Have two pointers, one at the head of list1 & second at the head of list 2
# Create a dummy node | call it result
# Now iterating till either of the pointer becomes None
# If left <= right, dummy.next = left & left = left.next
# else dummy.next = right & right = right.next
# At the end check if either of the list has values (not Null), append to the end
# set head to dummy.next
# return head
# Time O(n + m) | Space O(1)

# def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#     left = list1
#     right = list2
#     dummy = ListNode()
#     curr = dummy
#     while left and right:
#         if left.val <= right.val:
#             curr.next = left
#             left = left.next
#         else:
#             curr.next = right
#             right = right.next
#         curr = curr.next
#     if left:
#         curr.next = left
#     if right:
#         curr.next = right
#     return dummy.next
