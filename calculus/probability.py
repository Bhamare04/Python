# def bayes_theorem(prior,likelihood,evidence):
#     return (likelihood * prior) / evidence

import numpy as np
import matplotlib.pyplot as plt
# mu,sigma = 0,1
# x =np.linspace(-4,4,100)
# y = (1/(np.sqrt(2*np.pi)*sigma)) * np.exp(-0.5*((x-mu)/sigma)**2)
# plt.plot(x,y)
# plt.title('Normal Distribution')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# print("x:",x)
# print("y:",y)

# p =0.6
# plt.bar([0,1],[1-p,p],color=['blue','orange'])
# plt.xticks([0,1],['Not Rain','Rain'])
# plt.title('Prior Probability of Rain')
# plt.ylabel('Probability')
# plt.show()

#binomial distribution
from scipy.stats import binom
# n = 10
# p = 0.5
# x = np.arange(0, n+1)
# y = binom.pmf(x, n, p)
# plt.bar(x, y)
# plt.title('Binomial Distribution')
# plt.xlabel('x')
# plt.ylabel('Probability')
# plt.show()

from scipy.stats import poisson
x= np.arange(0, 10)
y = poisson.pmf(x, mu=3)
plt.bar(x, y)
plt.title('Poisson Distribution')
plt.xlabel('x')
plt.ylabel('Probability')
plt.show()