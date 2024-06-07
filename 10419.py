for _ in range(int(input())):
    d=int(input())
    zigak=0
    while(zigak+zigak**2<=d): zigak+=1
    print(zigak-1)