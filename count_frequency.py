# l1 = [3,4,2,3,2,5,6]

# for i in l1:
#     print(i,l1.count(i))

#count vowels in a string
# a = input("enter a string:")
# for i in a:
#     if i in "aeiouAEIOU":
# #         print(i,a.count(i))

# #factorial of a number
# a = int(input("enter a number:"))
# fact = 1
# for i in range(1,a+1):
#     fact=  fact * i
#     print("factorial is",fact)

#remove duplicates from a list
l1 = [3,4,2,3,2,5,6]
print(set(l1))

#sort a list
# l1 = [3,4,2,3,2,5,6]
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]>l1[j]:
#             l1[i],l1[j] = l1[j],l1[i]
# print(l1)

#find 2nd largest number in a list
# l1 = [3,4,2,3,2,5,6]
# l1 = list(set(l1))
# l1.sort()
# print(l1[-2])