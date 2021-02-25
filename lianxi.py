#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :lianxi.py
# @Time      :2020/11/23 17:16
# @Author    :HBB

#
# a=1+1
# print(a)

# a=5-4
# print(a)

# a=9//3
# print(a)

# a=9%5
# print(a)

# a,b,c,=1,2,3,
# print(a)
# print(b)
# print(c)


# age=int(input("请输入您的年龄："))
# if age>=18:
#     print("老板请进，祝您玩的愉快")
# else:
#     print("你丫的的年龄达不到，滚蛋")


# age=int(input("请输入您的年龄"))
# if age<18:
#     print("小屁孩，打什么工，回去写作业吧")
# elif 60>=age>=18:
#     print("您属于合法年龄，可以上班")
# else:
#     print("您老了，别干了，退休吧")



for a in range(1,10):
    b=1
    for b in range(b,a+1):
        print(f"{a}*{b}={a*b}",end="\t")
        b+=1
    print()
    a+=1


#
# a=int(input("输入边长a："))
# b=int(input("输入边长b："))
# c=int(input("输入边长c："))
# if a+b>c:
#     if a ^ 2 + b ^ 2 == c ^ 2:
#         print("该三角形为直角三角形")
#     elif a ^ 2 + b ^ 2 < c ^ 2:
#         print("该三角形为钝角三角形")
#     elif a ^ 2 + b ^ 2 > c ^ 2:
#         print("该三角形为钝角三角形")
# else:
#     print("该三角形不成立")





# age=20
# if age<=18:
#     print("年龄不够不能上网")
# else:
#     print("可以上网")

# money=int(input("请投币:1 or o"))
# if money==1:
#     print("请上车")
#     seat = int(input("是否有座位:1 or 0"))
#     if seat==1:
#         print("请坐")
#     else:
#         print("不好意思没有座位")
# else:
#     print("没有投币不能上车")



# import random
# player=int(input("请输入相应的数字:0-石头,1-剪刀,2-布"))
# computer=random.randint(0,3)
# print(computer)
# if ((player==0)and(computer==1)or(player==1)and(computer==2)or(player==2)and(computer==0)):
#     print("玩家获胜")
# elif player==computer:
#     print("打平了")
# else:
#     print("电脑获胜")


# i=1
# while i<5:
#     print("aaa")
#     i+=1
# print('结束')

# i=1
# sum=0
# while i <=100:
#     sum+=i
#     i+=1
# print(sum)

# i=1
# sum=0
# while i<=100:
#     if i%2==0:
#         sum+=i
#     i+=1
# print(sum)

# i=1
# sum=0
# while i<=100:
#     if i%2!=0:
#         sum+=i
#     i+=1
# print(sum)

# sum=0
# for i in range(0,101,2):
#     sum+=i
# print(sum)
#
# sum=0
# for i in range(1,101,2):
#     sum+=i
# print(sum)

#
# i=1
# while i <=5:
#     if i == 3:
#         print(f"我吃饱了，不吃了")
#         break
#     print(f"我吃了{i}个苹果")
#     i+=1
#
#
# i=1
# while i <=5:
#     if i==3:
#         print(f"吃出来个虫子，换一个")
#         i+=1
#         continue
#     print(f"吃了第{i}个")
#     i+=1



# a=["a","b","c","d"]
# print(".".join(a))
# print("+".join(a))

# a="hello world"
# print(a.upper())
# print(a.lstrip())
# print(a.rstrip())
# print(a.strip())
# print(a.ljust(20,"."))
# print(a.rjust(39,"."))
# print(a.center(41,"."))

















































































































