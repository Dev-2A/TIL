# 반복문을 이용하여 피라미드를 그리시오 (??????????????????????????????????????????????????????)

for i in range(1,6):
    print("*" * i)

print("=" * 5)

# 맨 마지막 요소는 스텝! 얼마나 커질 거냐(작아질 거냐) 단위!
for j in range(5,0,-1):
    print("*" * j)

print("=" * 5)

for k in range(1,6):
    print(" " * (5-k), "*" * k)

print("=" * 5)

for l in range(5,0,-1):
    print(" " * (5-l), "*" * l)

print("=" * 5)

# 파이썬은 기본 실수형!! int 지정 안 해주면 4.0, 3.0으로 처리되면서 * 연산이 통하지 않음!!
for m in range(1,10,2):
    print(" " * int((9-m)/2), "*" * m, " " * int((9-m)/2))