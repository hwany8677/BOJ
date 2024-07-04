#웰노운
#(7,3) -> (1) (2) 3 (4) (5) 6 (7) (1) 2 (4) (5) 7 (1) (4) 5 (1) (4) 1 (4) (4) 4
def checkTable(table):
    c=0
    length=len(table)
    for element in table: c+=1 if not(element) else 0
    return False if c==length else True
n,k=map(int,input().split())
table=[True for _ in range(n)] #카운트를 줄이는 용도로
#리스트 참조는 (i-1)번째로.
#True이면 1 줄이고, False이면 유지
#만약 한바퀴를 다 돌았다면 다시 i를 1로 복귀
i=1
copy_k=k-1
how_many_times=0
print("<",end='')
while (checkTable(table)):
    if copy_k==0 and table[i-1]:
        table[i-1]=False
        copy_k=k-1
        print(f"{i}, " if how_many_times<6 else f"{i}>",end='')
        i=i+1 if i!=n else 1
        how_many_times+=1
        continue 
    if table[i-1]: copy_k-=1
    i=i+1 if i!=n else 1
print()