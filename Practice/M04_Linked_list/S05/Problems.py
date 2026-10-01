#876. Middle of the Linked List
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        curr = head
        for _ in range(length // 2):
            curr = curr.next
            
        return curr
#Method2
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
#141. Linked List Cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        temp = head 
        while temp:
            if temp in visited:
                return True
            visited.add(temp)
            temp = temp.next
        return False
#2Method
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head  
        while fast and fast.next:
            slow = slow.next          
            fast = fast.next.next     
            if slow == fast:        
                return True         
        return False
#19. Remove Nth Node From End of List
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        count = 0
        temp = head
        while temp:
            count+=1
            head = temp.next
        dummy = ListNode()
        dummy.next = head
        temp = dummy
        for i in range(count-n):
            temp - temp.next
        temp.next = temp.next.next
        return dummy.next
#21. Merge Two Sorted Lists
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if not list1:
            return list2
        if not list2:
            return list1
            
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        new_node = ListNode()
        temp = new_node
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
        else:
            temp.next = list2