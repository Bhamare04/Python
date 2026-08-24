set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "kiwi", "orange"}

set1.add("mango")
print(set1)

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1 & set2)