# for문 2개를 이용하여 1부터 16까지 4 * 4 로 표시하시오

# for문 안의 i, j 등의 변수 값은 진짜 개위급상황 아닌 이상 바뀌면 안됨

for j in range(1,5):
    for i in range(1,5):
        print(i+(j-1)*4, end='\t')
    print("\n")
    
print("=" * 5)

for k in range(4,0,-1):
    for m in range(4,0,-1):
        print(m+(k-1)*4, end='\t')
    print("\n")