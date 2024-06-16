box=list(map(int,input().split()))
h=[box[len(box)-2],box[len(box)-1]]
box.remove(box[len(box)-2])
box.remove(box[len(box)-1])
box.sort()
res=[]
for bx in range(2):
    doBreak=False
    for i in range(len(box)-2):
        for j in range(i+1,len(box)-1):
            for k in range(j+1,len(box)):
                s=box[i]+box[j]+box[k]
                if s==h[bx]:
                    print(box[k],box[j],box[i],'',end='')
                    box.remove(box[k])
                    box.remove(box[j])
                    box.remove(box[i])
                    doBreak=True
                    break
            if doBreak: break
        if doBreak: break