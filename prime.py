
# sosu=int(input("***숫자를 입력하세요:"))
# a=0

# if sosu==1:
#     print("1은 소수가 아닙니다.")

# elif sosu!=1:
#     for i in range(2,sosu):
#         if sosu%i==0:
#             a=1
#             break
#         else:
#             a=0

#     if a==1:
#         print("%d는 소수가 아닙니다."%sosu)

#     else:
#         print("%d는 소수입니다."%sosu)

a=int(input("숫자를 입력하세요"))
b=0
if a==1:
    print("소수가 아닙니다")
else:
    for i in range(1,a):
        if a%i==0:
            b=1
        if b==0:
            print("소수입니다")
        else:
            print("소수가 아닙니다")