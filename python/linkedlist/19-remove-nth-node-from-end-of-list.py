from typing import List, Optional

'''
问题：
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
解题思路:
快慢指针
推导过程:
无
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def generate(self, data=[]):
        if data:
            self.val = data[0]
            preivous = self
        for i in range(1, len(data)):
            current = ListNode(data[i])
            preivous.next = current
            preivous = current
        return self
        

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        previous = None
        current = head
        pos = head
        result = None
        for i in range(n):
            current = current.next
        
        while current:
            previous = pos
            pos = pos.next
            current = current.next
        if previous:
            previous.next = pos.next
            result = head
        else:
            result = head.next
        return result


def test1():
    nums = [1,2]
    n = 1
    head = ListNode().generate(nums)
    head = Solution().removeNthFromEnd(head, n)
    while head:
        print(head.val)
        head = head.next

if __name__ == '__main__':
    test1()