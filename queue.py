
que=[]
def enqueue_ele():
    if len(que)==n:
        print('full')
    else:
        ele=int(input('ent ele:'))
        que.append(ele)
        print(que)
def dequeue_ele():
    if len(que)==0:
        print('empty')
    else:
        e=que.pop(0)
        print(e,'removed sucessfully')
        print(que)
n=int(input('ent size:'))
while True:
    print('sel oprn 1.enqueue 2.dequeue 3.exit')
    opn=int(input())
    if opn==1:
        enqueue_ele()
    elif opn==2:
        dequeue_ele()
    else:
        print('invalid')
