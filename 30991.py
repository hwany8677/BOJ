#exsinxcosx, excos^2x, exsin^2x => f(x), g(x), h(x)
#ESC(n)(x)=anf(x)+bng(x)+cnh(x) (n: times diff'd)
n=int(input())
esc,ec2,es2=1,0,0 #cn,bn,an
for i in range(n):
    original_esc=esc #ec2와 es2가 계산되는 과정에서 덮어씌워짐을 막기위함 (이거 못찾아서 시간개날림 ㅅㅂ)
    if ec2!=0:
        esc+=ec2*(-2)
    if es2!=0:
        esc+=es2*(2)
    if esc!=0:
        ec2+=original_esc
        es2+=-original_esc
print(esc+es2+ec2)