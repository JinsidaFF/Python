
import   datetime   #使用datetime库

def getDate(releaseDate,day): #定义getDate函数
    c=releaseDate.split("-")  #对输入的日期进行切片生成列表["年","月","日"]
    return datetime.date(int(c[0]),int(c[1]),int(c[2])) + datetime.timedelta(days=int(day)) #返回过期时间(日期+保质期(天))
    
d = input() 
a=d.split(",") #对输入进行切片["日期","保质期"]
x=a[0]  #函数第一个变量为日期
y=a[1]  #函数第二个变量为保质期
print(getDate(x,y))
