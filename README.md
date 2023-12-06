import random
q = True
w = False
print("로또 번호를 입력하시오.")
a,b,c,d,e,f = map(int,input("숫자를 띄어쓰기를 기준으로 입력해주세요.\n").split())
print(a,b,c,d,e,f)
an = random.randrange(1,45)
bn = random.randrange(1,45)
cn = random.randrange(1,45)
dn = random.randrange(1,45)
en = random.randrange(1,45)
fn = random.randrange(1,45)


int(an)
int(cn)
int(bn)
int(dn)
int(en)
int(fn)
a결과 = 0
b결과 = 0
c결과 = 0
d결과 = 0
e결과 = 0
f결과 = 0
print(an,bn,cn,dn,en,fn)
if a == an:
    a결과 = True
if b == bn:
    b결과 = True
if c == cn:
    c결과 = True
if d == dn:
    d결과 = True
if e == en:
    e결과 = True
if f == fn:
    f결과 = True
if a결과 == True:
    print('채점중...')
if b결과 == True:
    print('채점중..')
if c결과 == True:
    print('채점중.')
if d결과 == True:
    print('채점중...')
if e결과 == True:
    print('채점중.')
if f결과 == True:
    print("당첨!")
