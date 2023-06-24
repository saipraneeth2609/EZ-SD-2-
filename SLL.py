class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:   
            print("list is empty")
        else:
            currentnode=self.head
            while currentnode.next:
                print(currentnode.data, end="->")
                currentnode=currentnode.next
            print(currentnode.data)
    def insert_at_beg(self, data):
        newnode= Node(data)
        newnode.next=self.head
        self.head=newnode
    def insert_at_last(self, data):
        newnode = Node(data)
        curr=self.head
        if self.head is None:
            print("list is empty")
        else:
            while curr.next:
                curr=curr.next
            curr.next=newnode
    def insert_position(self,pos,data):
        newnode=Node(data)
        curr=self.head
        for i in range(pos-1):
            curr=curr.next
        newnode.next=curr.next
        curr.next=newnode
    def delete_beginning(self):
        curr=self.head
        self.head=curr.next
        curr.next=None
    def delete_end(self):
        curr=self.head.next
        prev=self.head
        while curr.next is not None:
            curr=curr.next
            prev=prev.next
        prev.next=None
        curr.prev=None
    def delete_position(self,pos,data):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
obj=SLL()
n=Node(1)
obj.head=n
n1=Node(2)
obj.head.next=n1
n2=Node(3)
n1.next=n2
n3=Node(4)
n2.next=n3
n4=Node(5)
n3.next=n4
n5=Node(6)
n4.next=n5
n6=Node(7)
n5.next=n6
obj.display()
obj.insert_at_beg(8)
obj.display()
obj.insert_at_beg(9)
obj.display()
obj.insert_at_last(10)
obj.display()
obj.insert_position(3,9)
obj.display()
obj.delete_beginning()
obj.display()
obj.delete_end()
obj.display()
obj.delete_position(3,2)
obj.display()
