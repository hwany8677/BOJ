#흰 검 흰 검 흰 검 흰 검
#검 흰 검 흰 검 흰 검 흰
board=["F","","F","","F","","F",""]
c=0
for _ in range(8):
  buf=input()
  for i in range(len(buf)): 
    if buf[i]==board[i]: c+=1
  board.reverse()
print(c)