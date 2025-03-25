array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i,0,-1):
        if array[j]<array[j-1]:
           array[j],array[j-1]=array[j-1],array[j]
        else:
            break

    
print(array)

"""
2번째 데이터 부터 시작하여 데이터를 비교 후 적절한 위치에 삽입
"""
