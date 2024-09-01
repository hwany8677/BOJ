from sys import stdin
input=stdin.readline
#음수 반올림에 주의
def half_round(n):
    temp=int(n*10)
    if temp>0:
        if temp%10<5: return temp//10
        else: return (temp//10)+1
    else:
        if temp%10>5: return (temp//10)+1
        else: return temp//10
buf=[]
mode=dict()
n=int(input())
for i in range(n): 
    temp=int(input())
    buf.append(temp)
    try: mode[temp]+=1
    except KeyError: mode[temp]=1
arith_mean=half_round(sum(buf)/len(buf))
buf.sort()
median=buf[int(len(buf)/2)]
rangE=buf[len(buf)-1]-buf[0]
print(arith_mean)
print(median)
mode_mx=max(list(mode.values()))
mode_keys=mode.keys()
has_mx=[]
for num in mode_keys:
    if mode[num]==mode_mx:
        has_mx.append(num)
has_mx.sort(reverse=True)
res=has_mx[len(has_mx)-2] if len(has_mx)>1 else has_mx[len(has_mx)-1]
print(res)
print(rangE)