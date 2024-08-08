n=input()
notFound=True
while (notFound):
    div=0
    for num in n: #24 -> 2와 4
        div+=int(num)
    if int(n)%div==0:
        notFound=False
    else:
        n=str(int(n)+1)
print(n)