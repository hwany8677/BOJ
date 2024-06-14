#윗줄 아랫줄 양 끝: 별 n개씩
#윗줄 아랫줄 중간: 별 (2n-3)개씩
#중간줄 처음: 공백 최대 i개 출력 후 별 (최고점이 2개인 경우는 없음)
#중간줄 2번째: 공백 (n-2)개 출력 후 별
#중간줄 3번째: 공백 j개 출력 (j=2n-5, j=-1 찍고 다시 올라감)
#만약 공백이 0이되는 줄이라면, 별을 출력하지 말것. 그 외에는 출력
#중간줄 4번째: 공백 (n-2)개 출력 후 별
#중간줄 반복횟수: (2n-3)번
n=int(input())
i=1
j=2*n-5
# print("i=0  ",end='')
print('*'*n+' '*(2*n-3)+'*'*n)
wasMid=False
for _ in range(2*n-3):
  # print(f"i={i}  ",end='')
  print(' '*i,end='')
  print('*',end='')
  print(' '*(n-2),end='')
  print('*',end='')
  print(' '*j if i!=n-1 else '',end='')
  print('*' if i!=n-1 else '',end='')
  print(' '*(n-2),end='')
  print('*')
  if i==n-1: wasMid=True
  i=i-1 if wasMid else i+1
  j=j+2 if wasMid else j-2
# print("i=0  ",end='')
print('*'*n+' '*(2*n-3)+'*'*n)