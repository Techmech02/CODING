import numpy as np

arr = np.array([41, 42, 43, 44])

x = arr[[True, False, True, False]]
arr1=np.arange(60).reshape((12,5))
print(arr1)
print(arr1.shape,arr.size)
print(arr1.T)
print(arr1.shape)
print(arr1[-10:-1:-1])
arr=np.random.randint(1,10,(2,3,5))
print(arr)
print(arr[0:2,0:2 , 2:3])