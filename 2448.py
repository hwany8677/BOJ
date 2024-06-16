#'하나의 큰 삼각형은 그 안의 세 개의 삼각형을 무조건 완성시켜야 한다'
#(어라 이중피동인가)
#골드날먹 도전
from math import sqrt
n=int(input()) #변의 길이
buf=[[' ' for _ in range(n+1)] for _ in range(n+1)]
