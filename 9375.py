#1가지에서 최대 n가지의 카테고리를 적용
#기어를 하나만 착용할 수 있음 = n
#두가지 -> 
input=open(0).readline
for _ in range(int(input())):
    n=int(input())
    category=dict()
    if n==0: print(1); continue
    for __ in range(n):
        name,cate=input().rstrip().split()
        if cate not in category: category[cate]=1
        else: category[cate]+=1
    cat_val=list(category.values())
    sigma=cat_val[0]+1
    for i in range(1,len(cat_val)):
        value=cat_val[i]
        sigma*=(cat_val[i]+1)
    print(sigma-1)