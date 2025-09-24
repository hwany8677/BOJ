from sys import setrecursionlimit
setrecursionlimit(5000) #1000글자일때 딱 걸려버리는 이슈가 터짐
str1=input()
str2=input()
#-1: Not visited, >=0: return value
dp_table=[[-1 for _ in range(len(str2)+1)] for __ in range(len(str1)+1)]
def lcs(s1,s2):
    len_s1=len(s1)
    len_s2=len(s2)
    if len_s1==0 or len_s2==0: return 0
    s1_end,s2_end=s1[len_s1-1],s2[len_s2-1]
    #각각의 분기점에서 dp 테이블을 참조
    if s1_end==s2_end: #Match
        if dp_table[len_s1-1][len_s2-1]==-1: #If undiscovered
            res=1+lcs(s1[:len_s1-1],s2[:len_s2-1]) #Discover
        else: 
            res=1+dp_table[len_s1-1][len_s2-1]
        dp_table[len_s1][len_s2]=res #and record
        return res
    else: #Doesn't match
        if dp_table[len_s1-1][len_s2]==-1:
            res1=lcs(s1[:len_s1-1],s2)

        else: res1=dp_table[len_s1-1][len_s2]

        if dp_table[len_s1][len_s2-1]==-1:
            res2=lcs(s1,s2[:len_s2-1])

        else: res2=dp_table[len_s1][len_s2-1]

        dp_table[len_s1][len_s2]=max(res1,res2)
        return max(res1,res2) #우리는 최장을 원하기 때문.

print(lcs(str1,str2))