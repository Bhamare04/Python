import numpy as np
#scaling of an array
#arr = np.array([1,2,3,4])
#print(arr + 10)

#Broadcasting

# matrix = np.array([[1,2,3],[4,5,6]])
# vector = np.array([1,0,1])
# print(matrix + vector)

#aggregation functions
# arr = np.array([[1,2,3],[4,5,6]])
# print(np.sum(arr))
# print(np.max(arr))
# print(np.min(arr))
# print(np.mean(arr))
# print(np.median(arr))
# print(np.std(arr))

arr = np.random.randint(1,51,size=(5,5))
#print(arr)
# 

#generate random float numbers between 1 and 10
float_arr = np.random.uniform(1, 10, size=(5, 5))
#normalize the array to be between 0 and 1
float_arr = (float_arr - np.min(float_arr)) / (np.max(float_arr) - np.min(float_arr))
print(float_arr)