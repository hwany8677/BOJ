#Everything needs to be checked separately
#(assuming inputs aren't that long)
input=open(0).readline
def char_check(passwd):
    #2 & 3. Lowercase & Uppercase check
    #4. Number check
    #5. Non-alphanumeric characters check
    ret=0
    lower,upper=0,0
    num,nonalpha=0,0
    for char in passwd:
        c=ord(char)
        if c>=65 and c<=90: upper+=1
        if c>=97 and c<=122: lower+=1
        if c>=48 and c<=57: num+=1
        if char=='!' or char=='@' or char=='#' or char=='$' or char=='%' or char=='^' or char=='&' or char=='*' or char=='.' or char==',' or char==';' or char=='/' or char=='?': nonalpha+=1 
    ret+=1 if upper>=2 else 0
    ret+=1 if lower>=2 else 0
    ret+=1 if num>=1 else 0
    ret+=1 if nonalpha>=2 else 0
    #print(f"upper={upper}, lower={lower}, num={num}, nonalpha={nonalpha}")
    return ret
def pali_consec_check(passwd):
    #6. Consecutive letters check
    ret=0
    consec,pali=1,1
    cur_char=''
    combo=0
    for char in passwd:
        if cur_char!=char: cur_char=char; combo=0
        elif cur_char==char: combo+=1
        if combo==3: consec=0; break
    #7. Palindrome check
    passwd=list(passwd)
    i=0
    while(i<len(passwd)):
        char=passwd[i]
        if not(char.isalpha()): passwd.pop(i)
        else: i+=1
    for i in range(len(passwd)//2):
        c_start=ord(passwd[i])
        c_end=ord(passwd[len(passwd)-1-i])
        if c_start>=65 and c_start<=90: c_start+=32
        if c_end>=65 and c_end<=90: c_end+=32
        if c_start==c_end: pali=0; break
    ret+=consec
    ret+=pali
    #print(f"consec={consec}, pali={pali}")
    return ret
def word_check(passwd,word):
    #8: Check if there's predefined words within the password
    ret=1 #1: not found, 0: found
    combo=0
    to_check=[ord(char) for char in word]
    idx=0
    for char in passwd:
        c=ord(char)
        if c>=65 and c<=90: c+=32
        if c==to_check[idx]: combo+=1; idx+=1
        if combo==len(word): ret=0; break
    #print(f"word_check's ret={ret}")
    return ret
def wordcheck_sigma(passwd):
    ret=0
    checklist=['password','virginia','cavalier','code','edoc','reilavac','ainigriv','drowssap']
    for check in checklist: ret+=word_check(passwd,check)
    return 1 if ret==8 else 0
for _ in range(int(input())):
    status=0 #Sum of all statuses must equal to 8
    passwd=input().rstrip()
    #1. Length check
    status+=1 if len(passwd)>=9 and len(passwd)<=20 else 0
    #print(f"status={status}")
    status+=char_check(passwd)
    #print(f"status={status}")
    status+=pali_consec_check(passwd)
    #print(f"status={status}")
    status+=wordcheck_sigma(passwd)
    #print(f"status={status}")
    print("Valid Password" if status==8 else "Invalid Password")
