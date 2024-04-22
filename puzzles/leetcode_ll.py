'''You are given two non-empty linked lists representing two non-negative integers. The digits 
   are stored in reverse order, and each of their nodes contains a single digit. 
   Add the two numbers and return the sum as a linked list.
   You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):  
        self.head = None

    def print(self):
        p = ''
        if not self.head:
            return
        else:
            current = self.head
            while current.next is not None:
                p += current.val
                current = current.next
            p += current.val
            print(p)

    def insert(self, node: ListNode):
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def get_item(self, val: str):
        if not self.head:
            return
        else:
            current = self.head
            while current.next is not None:
                if current.val == val:
                    return current
                current = current.next
                
    def add_values_reverse(self):
        if not self.head:
            return
        else:
            r = ''
            current = self.head
            while current.next is not None:
                if current.val >= 0:
                    r += str(current.val)
                    current = current.next
            r += str(current.val)
        return r[::-1]
        
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll1 = LinkedList()
        ll1.insert(l1)
        ll2 = LinkedList()
        ll2.insert(l2)
        l1_total_s = ll1.add_values_reverse()
        l2_total_s = ll2.add_values_reverse()
        total = int(l1_total_s) + int(l2_total_s)
        final_list = LinkedList()
        total = str(total)
        for c in str(total):
            final_list.insert(ListNode(val=int(c)))
        return final_list.head


        
if __name__ == "__main__":
        s = Solution()
        first = ListNode(val=1)
        second = ListNode(val=0)
        first.next = second
        third = ListNode(val=9)
        second.next = third

        first1 = ListNode(val=5)
        second1 = ListNode(val=7)
        third1 = ListNode(val=8)
        # fourth = ListNode(val=9)
        
        first1.next = second1
        second1.next = third1
        # third1.next = fourth
        r = s.addTwoNumbers(first, first1)
        while r.next is not None:
            print(r.val)
            r = r.next
        print(r.val)
