n=int(input())
m=int(input())
s=input()
streak=0
count=0
i=0
io_witness=False
wasnt=True
# print(f"Looking: i={i}, letter={s[i]}")
# print(f"**** COUNTED **** (count={count})")
# print(f"**** FINAL COUNT **** (count={count})")
# print(f"Streak updated! streak={streak}")
while(i<m):
    # print(f"Looking: i={i}, letter={s[i]}")
    #### KNOW YOUR PATTERNS ####
    # (Increase i by 2 unless specified)
    # 1. 'IO' -> streak++, always
    # 2. 'OI' -> Pause, add streak to count by (streak-1)-(n-1) if io_witness is True AND streak>=n.
    #            Increase i by 1 and reset streak regardless of previous instruction.
    # 3. 'OO' -> Pause, add streak to count by (streak-1)-(n-1) if io_witness is True AND streak>=n.
    #            Increase i by 1 and reset streak regardless of previous instruction.
    # 4. 'II' -> Pause, add streak to count by streak-(n-1) if io_witness is True AND streak>=n.
    #            Increase i by 1 and reset streak regardless of previous instruction.
    # 5. When i==m-2, use 1~4 as usual.
    # 6. When i==m-1:
    # 6-1. 'I' -> Add streak to count by streak-(n-1) if io_witness set to True AND streak>=n.
    # 6-2. 'O' -> Add streak to count by (streak-1)-(n-1) if io_witness set to True AND streak>=n.
    if i==m-1:
        if s[i]=='I': 
            if streak>=n and io_witness: 
                count+=streak-(n-1)
            i+=1
        elif s[i]=='O':
            if streak>=n and io_witness: 
                count+=(streak-1)-(n-1)
            i+=1
        # print(f"**** FINAL COUNT **** (count={count})")
        wasnt=False
    else:
        if s[i]=='I' and s[i+1]=='O':
            streak+=1
            # print(f"Streak updated! streak={streak}")
            io_witness=True
            i+=2
            continue
        if s[i]=='O' and s[i+1]=='I':
            if streak>=n and io_witness: count+=(streak-1)-(n-1)
            i+=1
            streak=0
            # print(f"**** COUNTED **** (count={count})")
            continue
        if s[i]=='O' and s[i+1]=='O':
            if streak>=n and io_witness: count+=(streak-1)-(n-1)
            i+=1
            streak=0
            # print(f"**** COUNTED **** (count={count})")
            continue
        if s[i]=='I' and s[i+1]=='I':
            if streak>=n and io_witness: count+=streak-(n-1)
            i+=1
            streak=0
            # print(f"**** COUNTED **** (count={count})")
            continue
if i==m and wasnt:
    i-=1
    if s[i]=='I': 
        if streak>=n and io_witness: 
            count+=streak-(n-1)
        i+=1
    elif s[i]=='O':
        if streak>=n and io_witness: 
            count+=(streak-1)-(n-1)
        i+=1
    # print(f"**** FINAL COUNT **** (count={count})")
print(count)