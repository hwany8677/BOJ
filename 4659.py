#'1' for check if there's at least one vowel,
#'2' for two consecutive occurences, 
#'3' for three consecutive vowels/consonants
def isAcceptable(s,mode): #False: does qualify, True: does not qualify
    length=len(s)
    if mode==1:
        count=0
        for c in s:
            if c in "aeiou": count+=1
        if count: return False
        else: return True
    if mode==2:
        for i in range(1,length):
            letter1=s[i-1]
            letter2=s[i]
            if letter1==letter2: #같을때  
                if letter1=='e' or letter1=='o': continue #'ee'와 'oo'는 스킵
                else: return True
        return False
    if mode==3:
        for i in range(2,length):
            letter1_type=s[i-2] in "aeiou"  #True: Vowel, False: Consonant
            letter2_type=s[i-1] in "aeiou"  
            letter3_type=s[i] in "aeiou"    
            #True True True -> not ac
            #False False False -> not ac
            #Everything else -> ac
            if letter1_type==letter2_type and letter2_type==letter3_type and letter3_type==letter1_type: return True
        return False
while(1):
    s=input()
    if s=="end": break
    if len(s)==1:
        if s not in "aeiou": print(f"<{s}> is not acceptable.")
        else: print(f"<{s}> is acceptable.")
    elif len(s)==2:
        if isAcceptable(s,1): 
            print(f"<{s}> is not acceptable.")
            continue
        if s[0]==s[1] and (s not in ["ee","oo"]): print(f"<{s}> is not acceptable.")
        else: print(f"<{s}> is acceptable.")
    else:
        if isAcceptable(s,1): print(f"<{s}> is not acceptable.")   #1st rule check
        elif isAcceptable(s,2): print(f"<{s}> is not acceptable.") #3rd rule check
        elif isAcceptable(s,3): print(f"<{s}> is not acceptable.") #2nd rule check
        else: print(f"<{s}> is acceptable.")