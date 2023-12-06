# # print(int(input())*int(input()))
# for i in range(1,10):
#     for j in range(1,19):
#         print(i*j,end=" ")
#     print(' ')

# a = int(input('몇단부터 시작하시겠습니까?>>>'))
# b = int(input('몇단으로 끝내시겠습니까?>>>'))
# x = [ ]
# for i in range(a,b):
#     for j in range(1,19):
#         d = i * j
#         print("%d"%i +"x"+"%d"%j +"="+"%d"%d)
#     print(' ')

# a = [1,2,3,4,5,6,7,8,9,10]
# result = []
# for num in a:
#     result.append(num * 3)
# print(result)

# result = [num * 3 for num in a]
# print(result)

def 더하기 (a,b):
    return a + b
def 빼기 (a,b):
    return a - b
def 곱하기 (a,b):
    return a * b
def 나누기 (a,b):
    return a / b 
def 나머지 (a,b):
    return a % b


a = int(input())
b = int(input())
c = (input())

if c == "*":
    print(곱하기(a,b))
if c == '-':
    print(더하기(a,b))
if c == '+':
    print(빼기(a,b))
if c == '/':
    print(나누기(a,b) + 나머지(a,b))



































































