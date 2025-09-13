input=open(0).readline
dot_list={
    "R":45,
    "G":30,
    "B":20,
    "Y":15,
    "O":10,
    "W":5
}
def rounding(price,payment):
    return float(f"{price:.2f}") if payment=='P' else float(f"{price:.1f}")
n=int(input())
for _ in range(n):
    og,dot,coupon,payment=input().rstrip().split() #C: round(,1), P: round(,2)
    og=float(og)
    dis=og*dot_list[dot]/100
    # dis=rounding(dis,payment)
    og-=dis
    # og=rounding(og,payment)
    if coupon=='C':
        dis=og/20
        # dis=rounding(dis,payment)
        og-=dis
        # og=rounding(og,payment)
    og=rounding(og,payment)
    print(f"${og:.2f}")