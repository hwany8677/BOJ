while(1):
    grade=list(map(int,input().split()))
    if sum(grade)==0: break
    grade.remove(min(grade))
    grade.remove(max(grade))
    avg=sum(grade)/4
    isInt=(avg%1.0)==0.0
    print(int(avg) if isInt else avg)