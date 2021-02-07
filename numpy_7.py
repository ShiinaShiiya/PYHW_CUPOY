import numpy as np

array1 = np.array([[10, 8], [3, 5]])

#1. 運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
print("反矩陣\n",np.linalg.inv(array1))
array2 = np.linalg.inv(array1)
print("矩陣乘法\n",np.matmul(array1, array2))

if len(array1) == len(array2):
    if np.eye(len(array1),len(array2), dtype=float).all() == np.matmul(array1, array2).all():
        print("是否為單位矩陣:是")
    else:
        print("是否為單位矩陣:否")

#2. 運用上列array計算特徵值、特徵向量?
eigenvalue,featurevector=np.linalg.eig(array1)
print("特徵值\n",eigenvalue)
print("特徵向量\n",featurevector)

#3. 運用上列array計算SVD?
u, s, vh = np.linalg.svd(array1)
print("u=", u)
print("s=", s)
print("vh=", vh)