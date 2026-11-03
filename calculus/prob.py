import numpy as np

rolls = np.random.randint(1,7,1000)

p_even = np.sum(rolls % 2 ==0)/len(rolls)
p_greater_4 = np.sum(rolls>4)/len(rolls)

print(p_even)
print(p_greater_4)