array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count=[0]*(max(array)+1) # 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)

for i in range(len(array)):
    count[array[i]]+=1 
    
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
