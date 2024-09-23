#Filthy code
#m-2일 때 구분하기 위해 많조분을 너무 남발함 (코드 가독성 매우낮음)
#IO면 스킵, I나 O면 그대로
#희대의 엣지케이스: IOII, IOOI, IOIO, OOIO, OIOI, OOII
n=int(input())
m=int(input())
s=input()
one_last_blow_check=False #n번째일때 발동 (∵ 'IO'가 반복되기 때문)
streak=0
count=0
i=0
io_witness=False
while(i<m):
    print(f"Looking: i={i}, letter={s[i]}")
    if i==m-1: 
        if s[i]=='I' and io_witness:
            count+=streak-(n-1)
            #print(f"**** FINAL COUNT **** (count={count})")
        if s[i]=='O' and io_witness:
            count+=1
        break 
    if i==m-2:
        if (s[i]=='I' and s[i+1]=='I') and io_witness:
            count+=streak-(n-1)
            #print(f"**** FINAL COUNT **** (count={count})")
            break
    if one_last_blow_check:
        if s[i]=='I': 
            count+=streak-(n-1)
            streak=0
            one_last_blow_check=False
            io_witness=False
            #print(f"**** COUNTED **** (count={count})")
            if i>m-3: break
            continue
        else:
            streak=0
            one_last_blow_check=False
            continue
    if s[i]=='I' and s[i+1]=='O':
        #이미 io_witness=True 전재해놓고 쓴것
        if i==m-2: 
            if io_witness:
                count+=streak-(n-1)
                #print(f"**** FINAL COUNT **** (count={count})")
            break
        streak+=1
        #print(f"Streak updated! streak={streak}")
        i+=2
        #print(f"next i={i}")
        io_witness=True
    else:
        if io_witness: one_last_blow_check=True; continue
        streak=0 
        i+=1
        io_witness=False
print(count)
