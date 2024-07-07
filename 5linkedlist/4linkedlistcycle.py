# https://leetcode.com/problems/linked-list-cycle/description/

# Approach:
# Two pointers, slow & fast. Slow goes one step at a time, fast goes two step at a time
# Since the slow one moves one step & fast one moves two steps, if there is a cycle, they are bound to meet.
# Use a while loop till fast reaches None
# Time O(n) | Space O(1)
# O(n) because the fast will reach the end in half the time of n
# And no matter where the loop connects, they are bound to meet before slow reaches the end

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         fast, slow = head, head
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#             if fast == slow:
#                 return True
#         return False
