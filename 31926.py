#다해노코 이루부러상!!!!!!!!!
#5+1+2+1+1=10 daldidalgo daldidan
#5+1+2+1*(n)+1+1=10+n daldidalgo*(n번) daldidan 
daldidalgo=8 #daldi=5, dal=1, go=2, 따라서 8
daldidan=2 #daldida=1, n=1, 따라서 2
n=int(input())
real_n=n
mx_daldidalgo=1 #Stack of daldidalgo (ex daldidalgodaldidalgo -> 2, daldidalgo*5 -> 5)
if n==1: 
    print(10)
    exit(0)
bam_yang_GANG=daldidalgo
n-=1
while(n>0):
    #print(f"Current daldidalgo count={mx_daldidalgo}")
    #print(f"Remaining daldidalgo to paste={n}")
    if mx_daldidalgo>=n:
        #print("Too much daldidalgo for remaining daldidalgo. Pasting remaining daldodalgos...")
        break
    else: 
        bam_yang_GANG+=1
        n-=mx_daldidalgo
        #print(f"Remaining daldidalgo deducted by {mx_daldidalgo}.")
        mx_daldidalgo+=mx_daldidalgo
        #print(f"Max daldidalgo update. Count is now {mx_daldidalgo}.")
    #print(f"bam_yang_GANG={bam_yang_GANG}")
    #print()
bam_yang_GANG+=daldidan
print(bam_yang_GANG if real_n%2 else bam_yang_GANG+1)















#떠나는 길에 네가 내게 말했지
#너는 바라는 게 너무나 많아
#잠깐이라도 널 안 바라보면
#머리에 불이 나버린다니까
#
#나는 흐르려는 눈물을 참고
#하려던 얘길 어렵게 누르고
#그래 미안해라는 한 마디로
#너랑 나눈 날들 마무리했었지
#(뚠-뚠-뚠-뚠---)
#달디달고달디달고달디단, 밤 양 갱, 밤 양 갱
#내가먹고싶었던건달디단, 밤 양 갱, 밤 양 갱 이야
#
#떠나는 길에 네가 내게 말했지
#너는 바라는게 너무나 많아
#아냐 내가 늘 바란 건 하나야
#한 개 뿐이야 달디단 밤 양 갱
#
#(뚜루 뚜루 뚜루 뚜루 뚜루 뚜루 띠리따라뿌)
#(뚜루 뚜루 뚜루 뚜루 뚜루루뿝)
#(뚜루 뚜루 뚜루 뚜루 뚜루 뚜루 삐리빠라뿝)
#(삐리빠라삐리삡뿝붑 빠라빠라삐라뿝)
#
#(뚠-뚠-뚠-뚠---)
#
#달디달고달디달고달디단, 밤 양 갱, 밤 양 갱
#내가먹고싶었던건달디단, 밤 양 갱, 밤 양 갱 이야
#
#상다리가 부러지고
#둘이서 먹다 하나가 쓰러져버려도
#나라는 사람을 몰랐던 너어언
#
#떠나가다가 돌아서서 말했지
#너는 바라는 게 너무나 많아
#아냐 내가 늘 바란 건 하나야
#한 개 뿐이야 달디단 밤 양 갱
#
#(뚜루 뚜루 뚜루 뚜루 뚜루 뚜루 띠리따라뿌)
#(뚜루 뚜루 뚜루 뚜루 뚜루루뿝)
#(뚜루 뚜루 뚜루 뚜루 뚜루 뚜루 삐리빠라뿝)
#(삐리빠라삐리삡뿝붑 빠라빠라삐라뿝)
