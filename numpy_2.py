import numpy as np

array1 = np.array(range(30))

print(array1)

resh_array = np.reshape(array1, (5,6))              #將下列清單(list1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")
array1 = np.array(range(30))

print(resh_array)

print(np.where(resh_array%6==1))                   #呈上題的array，找出被6除餘1的數的索引