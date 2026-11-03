import numpy as np

# m1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# m2 = np.array([[2,3,4,6],[7,8,2,1],[3,4,5,6]])
# print(m1 * m2,end='\n\n')
# print(m1 + m2,end='\n\n')
# print(m1 - m2,end='\n\n')
# #print(m2)
# print(np.transpose(m1))

#normalize the matrix,scale the values to be between 0 and 1
# m1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# m2 = (m1 - np.min(m1)) / (np.max(m1) - np.min(m1))
# print(m2)


#generate a random array and find min and max values
array = np.random.rand(10,4)
print(np.min(array))
print(np.max(array))