#QuattroCheeze🅱izza
#n개의 토핑 중 서로 다른 치즈가 n개 있어야함
n=int(input())
cheeses=[]
toppings=input().split()
#Toppings check
for topping in toppings:
    count=0 #Cheese count
    j=5
    for i in range(len(topping)-1,-1,-1):
        if topping[i]=="Cheese"[j]: 
            if j==0: count+=1 #IT IS A CHEESE!!!
            j-=1
        else: break
    