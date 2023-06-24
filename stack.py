stack=[]

def push_ele():
    if len(stack)==n:
        print('Full')
    else:
        ele=int(input("enter ele"))
        stack.append(ele)
        print(stack)
def pop_ele():
    if len(stack)==0:
        print('empty')
    else:
        stack.pop()
        print(stack)
        
n=int(input("enter the size of stack"))
while True:
    print('select operation 1.push 2.pop 3.quit')
    operation=int(input())
    if operation==1:
        push_ele()
    elif operation==2:
        pop_ele()
    elif operation==3:
        break
    else:
        print("invalid")


    
