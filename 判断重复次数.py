
def testReEle(lis):
    c=0                     #计数器初始化为0
    while len(lis)!=0:      #循环，对列表内每一个元素进行判断
        b=lis[0]            #保存表第一个元素
        lis.remove(lis[0])  #删除列表第一个元素
        if b in lis:        #判断删除这一个元素之后列表内是否还有相同元素
            c+=1            #若存在相同元素则计数器加1
        else:
            c+=0            #若不存在计数器加0
    if c==0:                #若列表内无重复元素输出False，否则输出True
        return False
    else:
        return True
            

lis = []
ch = input() #"请输入判定元素，#表示结束："
while ch != '#':
    lis.append(ch)
    ch = input()   #"请输入判定元素，#表示结束："
if testReEle(lis):
    print("True")
else:
    print("False")
