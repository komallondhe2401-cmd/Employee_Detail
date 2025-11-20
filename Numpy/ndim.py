import numpy as np

arr1=np.array([1,2,3,4])
arr2=np.array([[1,2],[3,4],[5,6]])

print(arr1.ndim)
print(arr2.ndim)

print(arr1.dtype)
float_arr=arr1.astype(float)
print(float_arr)
print(float_arr.dtype)

print(arr1[[0,3]])
reshaped_arr=arr1.reshape(2,2)
print(reshaped_arr)
print(arr2.ravel())
print(arr2.flatten())

# Advance reshaping
# INSERT
new_arr=np.insert(arr1,2,100,axis=0)
print(new_arr)

new_2d_arr=np.insert(arr2,1,[10,20],axis=0)
print(new_2d_arr)

#Stacking
arr3=np.array([[1,2],[4,5]])
arr4=np.array([5,5,6,7])
# print(np.hstack((arr3,arr4)))

# Spliting
print(np.vsplit(arr3,2))
print(np.hsplit(arr3,2))




# BROADCASTING

matrix=np.array([[1,2,3],[4,5,6]])
vector=np.array([10,20,30])
a=4
result=matrix+vector
result1=matrix*a
print(result1)
print(result)