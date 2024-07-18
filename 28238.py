#PyPy3 took 624ms to run
#Meanwhile Python 3 took 1128ms to run
#매모리를 더 먹는방향으로 설계
#월화, 월수, 월목, 월금, 화수, 화목, 화금, 수목, 수금, 목금에 대한 상태를 싹다만듬
from sys import stdin
input=stdin.readline
n=int(input())
class_type=[0 for _ in range(10)] #월화, 월수, ..., 목금
for _ in range(n):
    buf=input().split()
    #if문 지옥의 시작
    if buf[0]=='1' and buf[1]=='1': class_type[0]+=1
    if buf[0]=='1' and buf[2]=='1': class_type[1]+=1
    if buf[0]=='1' and buf[3]=='1': class_type[2]+=1
    if buf[0]=='1' and buf[4]=='1': class_type[3]+=1
    if buf[1]=='1' and buf[2]=='1': class_type[4]+=1
    if buf[1]=='1' and buf[3]=='1': class_type[5]+=1
    if buf[1]=='1' and buf[4]=='1': class_type[6]+=1
    if buf[2]=='1' and buf[3]=='1': class_type[7]+=1
    if buf[2]=='1' and buf[4]=='1': class_type[8]+=1
    if buf[3]=='1' and buf[4]=='1': class_type[9]+=1
class_type_str=["1 1 0 0 0","1 0 1 0 0","1 0 0 1 0","1 0 0 0 1","0 1 1 0 0","0 1 0 1 0","0 1 0 0 1","0 0 1 1 0","0 0 1 0 1","0 0 0 1 1"]
mx=max(class_type)
print(mx)
print(class_type_str[class_type.index(mx)])