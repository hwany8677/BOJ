#'설마 이거?' 라고 생각하고 접근
def consec_sigma(n):
    mx,mx_buf=0,[]
    for i in range(1,n+1):
        sigma=0
        buf=[j for j in range(i,n+1)]
        for j in range(1,i): buf.append(j)
        for start in range(n):
            for end in range(start,n):
                sigma+=sum(buf[start:end])
        if sigma>mx: 
            mx=sigma
            mx_buf=buf
    return mx_buf,f"{n}: {mx_buf} {mx}"
n=int(input())
