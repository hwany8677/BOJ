input=open(0).readline
n=int(input())
char_sep=input().rstrip().split()
m=int(input())
num_sep=list(map(str,input().split()))
k=int(input())
#comb에 있는 내용을 기반으로 char_sep와 num_sep에서 빼야함
comb=input().rstrip().split()
len_s=int(input())
s=list(input().rstrip())
#리턴할 인덱스가 없을때까지 반복
for element in comb:
    if element.isalpha(): 
        try: 
            while(1):
                idx=char_sep.index(element)
                char_sep.pop(idx)
        except ValueError: continue
    else:
        try:
            while(1):
                idx=num_sep.index(element)
                num_sep.pop(idx)
        except ValueError: continue
#마찬가지로 리턴할 인덱스가 없을때까지 반복
res=['']
pos=0
for char in s:
    if char==' ': res.append('')
    elif char in char_sep: res.append('')
    elif char in num_sep: res.append('')
    else: 
        res[pos]+=char
        continue
    pos+=1
try:
    while(1):
        idx=res.index('')
        res.remove('')
except ValueError: pass
for element in res:
    for char in element: print(char,end='')
    print()