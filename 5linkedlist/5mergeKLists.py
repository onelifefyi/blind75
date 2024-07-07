# https://leetcode.com/problems/merge-k-sorted-lists/

# Brute:
# Take the first list, attach entire second list, keep going till no other list is left
# Time O(k.n) | space O(n) | where n is total number of nodes & k is the number of lists

# Approach:
# Follow like a merge sort | Divide & conquer
# Create a new list merged_list = []
# For each two items in the original list, merge them & push it to merged_list
# Each time repeat till merged list size becomes one

# Time O(nlogk) where n is total nodes & k is the #lists | Space O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#     if not lists:
#         return None
#
#     def merge(l1, l2):
#         dummy = ListNode()
#         curr = dummy
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 curr.next = l1
#                 l1 = l1.next
#             else:
#                 curr.next = l2
#                 l2 = l2.next
#             curr = curr.next
#         if l1:
#             curr.next = l1
#         else:
#             curr.next = l2
#         return dummy.next
#
#     while len(lists) > 1:
#         merged_list = []
#         for i in range(0, len(lists), 2):
#             l1 = lists[i]
#             l2 = lists[i + 1] if (i + 1) < len(lists) else None
#             merged_list.append(merge(l1, l2))
#         lists = merged_list
#
#     return lists[0]
