# 아래 식을 while 문으로 변경
# for i in range(1,6):
#     for j in range(1,6):
#         print(((j-1)*5)+i, end='\t')
#     print("\n")

# i = 0
# while i < 5:
#     i += 1
#     j = 0
#     while j < 5:
#         j += 1
#         print(((j-1)*5)+i, end='\t')
#     print("\n")
#     if i >= 5:
#         print("-"*5, "end", "-"*5)
        
###########################
# 선택정렬(Selection Sort)
# 배열에서 가장 작은 값을 찾아서 차례대로 앞으로 넘기면서 정렬하는 방법
# O(n)
###########################

list = [9,4,7,6,1]
sortedList = []
# print(list[:0]) # []
# print(list[0:]) # [9,4,7,6,1]
# print(list[:-1]) # [9,4,7,6]
# print(list[-1:]) # [1]
# print(list[0:-1])
# print(list[-1])
# list.insert(0,2)
# print(list)
# print(list.index(list[-1]))


for i in range(0, len(list)+1):
    j = 0
    while j <= len(list):
        for item in list:
            if item == min(list):
                sortedList.append(item)
                list.remove(item)
        j += 1
        if j >= len(list)+1:
            break

print(sortedList)