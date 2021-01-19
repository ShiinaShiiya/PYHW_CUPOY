import numpy as np

array1 = np.array(range(30))
array2 = np.array([2,3,5])

#. 將下兩列array存成npz檔
with open('work.npz', 'wb') as f:
    np.savez(f, a=array1, b=array2)

ans = np.load('work.npz')


print(ans['a'])
print(ans['b'])


