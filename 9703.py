#See something is non-decreasing or non-increasing
for i in range(int(input())):
    n=int(input())
    buf=list(map(int,input().split()))
    exists=False
    for j in range(n):
        current_num=buf[j]
        
        number_watch=current_num+1
        count=1
        for k in range(j+1,n): #Increasing
            if number_watch==buf[k]: 
                count+=1
                number_watch+=1
            if count==3:
                exists=True
                break
        if exists: break
        
        number_watch=current_num-1
        count=1
        for k in range(j+1,n): #Decreasing
            if number_watch==buf[k]: 
                count+=1
                number_watch-=1
            if count==3:
                exists=True
                break
        if exists: break

    print(f"Case #{i+1}:", "NO" if exists else "YES")