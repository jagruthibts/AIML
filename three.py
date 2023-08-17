import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print("sum of the array=",arr.sum())
print("maximun of the array =",arr.max())
print("minimum of the array =",arr.min())
print("cumilattive of the array=",arr.cumsum())
print("average of the array=",arr.mean())
print(arr.min(axis=1))
print(arr.max(axis=1))
