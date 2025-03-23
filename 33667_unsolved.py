# 연도
# -> 1년부터 99999999년까지 O(n)으로 윤년 전처리?

# 일단 구하는 단위가 Year인 경우 366일도 365일도 전부 1 Year임.
# 시간단위의 엄밀함은 필요가 없음 -> 일 단위만 보기.

# 그러므로 윤년이면 366일, 평년이면 365일이므로

# 1월 1일부터 해당 날짜까지 걸린 일수를 계산하고, 이를 365일(366일)로 나누기.
# =20xx.yy년이 나옴.

# 구하는 단위가 Month인 경우 

#12개월 = 윤년이든 아니든 언제든지 12월
input=open(0).readline
for _ in range(int(input())):
    born=list(map(int,input().split()))
    today=list(map(int,input().split()))
    unit=input().rstrip()
    