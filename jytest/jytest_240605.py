# for문 하나를 사용하여 구구단을 작성하시오

# # 1단
# for j in range(1,10):
#     for i in range(1,4):
#         print(i,"*",j,"=",i*j, end='\t')
#     print("\n")

for n in range(1,4):
    for l in range(1,10):
        for m in range(1,4):
            print(((n-1)*3)+m,"*",l,"=",(((n-1)*3)+m)*l, end='\t')
        print("\n")
    print("-"*25)