"""
本节程序功能:
1:让用户输入数据来新增学生数据节点,并建立一个单向链表
2:可以遍历链表并显示其内容
3:可求出当前链表不同成绩的平均分
单向链表定义:
    单向链表节点基本由两个元素组成(数据字段和指针),指针会指向下一个元素在内存中的地址


"""
#声明一个学生成绩链表节点的结构声明
class Student:
    def  __init__(self):
        self.Name=''
        self.Math=0
        self.Eng=0
        self.no=''
        self.next=None
"""
节点类的声明完成后就可以动态的建立链表中的每个节点
每新增一个节点,且ptr指向链表的第一个节点的四个步骤:
1:动态分配内存空间给新节点
2:将原链表的尾部指针(next)指向新的元素所在的内存地址
3:将ptr指针指向新节点的内存位置,表示这是新的链表尾部
4:由于新节点为当前链表的最后一个元素,因此将他的指针指(next)向None

"""

head=Student()#建立链表头部
head.next=None#当前无下一个元素
ptr=head #设置存取指针的位置
Msum=Esum=num=Student_no=0
select=0

while  select!=2:
    print("(1)新增(2)离开=>")
    try:
        select=int(input("请输入一个选项"))
    except ValueError:
        print("输入错误")
        print("请重新输入"+"\n")
    if select==1:
        new_data=Student()#新增下一个元素
        new_data.name=input("姓名")
        new_data.no=input("学号")
        new_data.Math=eval(input("数学成绩"))
        new_data.Eng=eval(input("英语成绩"))
        ptr.next=new_data #指针指向new_data
        new_data.next=None#new_data无下一个元素
        ptr=ptr.next #ptr移往下一个元素
#链表的遍历
ptr=head.next
print()
while ptr!=None:
    print('姓名:%s\t 学号:%s\t数学成绩:%d\t英语成绩:%d\t'\
          %(ptr.name,ptr.no,ptr.Math,ptr.Eng))
    Student_no=Student_no+1
    Msum=Msum+ptr.Math
    Esum=Esum+ptr.Eng
    ptr=ptr.next
#链表中求平均成绩
if  Student_no!=0:
    print("-"*50)
    print('本链表中学生的平均数学成绩是:%.2f  英语平均成绩是:%.2f'%(Msum/Student_no,Esum/Student_no))
