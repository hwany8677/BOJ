for _ in range(int(input())):
    score=list(map(int,input().split()))
    mi,mx=min(score),max(score)
    score.sort()
    #C에선 리스트 탐색 후 일일히 제거해줘야함 (-1로 지정하는 등등)
    score.remove(min(score))
    score.remove(max(score))
    largerThan4=False
    for i in range(len(score)):
        for j in range(i+1,len(score)):
            if largerThan4: break
            if score[j]-score[i]>3: largerThan4=True
        if largerThan4: break
    if largerThan4: print("KIN")
    else: print(sum(score))