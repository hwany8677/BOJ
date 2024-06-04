for n in range(int(input())):
    a,b,c=map(int,input().split())
    #If any one of them qualifies pythagorean theorem, print yes, otherwise no
    print(f"Scenario #{n+1}:")
    if (a**2+b**2==c**2 or b**2==a**2+c**2 or a**2==b**2+c**2): print("yes")
    else: print("no")
    print()