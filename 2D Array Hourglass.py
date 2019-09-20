import numpy as np

arr = np.array([[1, 1, 1, 0, 0, 0],
[0, 1 ,0, 0, 0, 0],
[1, 1 ,1 ,0, 0 ,0],
[0 ,0 ,2 ,4, 4 ,0],
[0 ,0 ,0 ,2, 0 ,0],
[0 ,0, 1 ,2, 4 ,0]])
sum = 0
max_sum = 0
for i in range(4):
    for j in range (4):
        sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        print('hourglass number for row',i,'is', sum)
        if sum> max_sum:
            max_sum = sum
print(max_sum)

