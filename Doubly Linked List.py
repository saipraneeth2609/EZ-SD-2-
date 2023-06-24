class Node:
    def __init__(self,data):
        self.previous=None
        self.data=data
        self.next=None
class DLL:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head is None:
            print("Doubly linked list is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end="->")
                temp=temp.next
    def insert_beg(self,data):
        new_node = Node(data)
        temp = self.head
        temp.previous = new_node
        new_node.next=temp
        self.head=new_node
    def insert_end(self,data):
        new_node = Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        new_node.previous=temp
    def insert_position(self,pos,data):
        new_node = Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new_node.previous=temp
        new_node.next=temp.next
        temp.next.previous=new_node
        temp.next=new_node
    def delete_begin(self):
        temp=self.head
        self.head=temp.next
        temp.next.previous=None
        temp.next=None
node_1 =Node("Apple")
print(node_1.next)
dl=DLL()
dl.head=node_1
print(dl.head)
print(dl.head.data)
node_2=Node("Ankitha")
print(node_2.data)
node_1.next=node_2
node_2.previous=node_1
print(node_1)
print(node_2)
print(node_1.next)
node_3=Node(3)
print(node_3.data)
node_2.next=node_3
node_3.previous=node_2
node_4=Node(4)
node_3.next=node_4
node_4.previous=node_3
print(node_4.data)
node_5=Node(5)
node_4.next=node_5
node_5.previous=node_4
#print(node_5.data)
#print(node_1.data,node_2.data,node_3.data,node_4.data,node_5.data)
#print(node_5.next)
#print(node_1.previous)
dl.display()
dl.insert_beg(7)
dl.display()
dl.insert_end(9)
dl.display()
dl.insert_position(3,5)
dl.display()
dl.delete_begin()
dl.display()
       
        
        
        
        
        
        
        
        

        
    
        
    