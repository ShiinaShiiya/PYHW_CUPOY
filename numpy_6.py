import numpy as np

array1 = np.array(range(30))
array2 = np.array([2,3,5])

#. 將下兩列array存成npz檔  work.npz
with open('work.npz', 'wb') as f:
    np.savez(f, a=array1, b=array2)

ans = np.load('work.npz')


print(ans['a'])
print(ans['b'])


#2. 讀取剛剛的npz檔，加入下列array一起存成新的npz檔   new_work.npz
array3 = np.array([[4,5,6],[1,2,3]])

np.savez('new_work.npz',ans['a'],ans['b'],array3)