from ds_lien_ket import UnorderedList,Node

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = 0

        #first init
        resNode = ListNode()
        copyNode = resNode
        
        #start iteration
        while(l1!=None or l2!=None or sum!= 0):
            print('l1',l1)
            if(l1!=None):
                sum += l1.val
                print('sum',sum)
                l1 = l1.next
           
            if(l2!=None):
                sum += l2.val
                l2 = l2.next
                print('sun',sum)
            newNode = ListNode()
            newNode.val = sum%10
            copyNode.next = newNode
            copyNode = newNode
            
            sum= int(sum/10)
        
        return resNode.next
o=Solution()
s=UnorderedList()
s.add(3)
s.add(4)
s.add(2)
k=UnorderedList()
k.add(4)
k.add(6)
k.add(5)
l1=s.ds_lk()
print(l1)
l2=k.ds_lk()
print(l2)
ds=[]
hien_tai=o.addTwoNumbers(l1,l2)
while hien_tai!=None:
    ds.append(hien_tai.val)
    hien_tai=hien_tai.next
print(ds)