import random
import os

n = int(input("请输入想产生多少个随机数："))
a = int(input("请输入随机数范围最小值："))
b = int(input("请输入随机数范围最大值："))

lst = [0] * n
for i in range(n):
    rnd = random.randint(a, b)
    while lst.count(rnd) != 0:
        rnd = random.randint(a, b)
    lst[i] = rnd

print("本轮产生的{}个幸运同学学号是：".format(n), lst)
os.system("pause")
