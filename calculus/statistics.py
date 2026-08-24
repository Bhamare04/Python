data = [10,20,30,40,50,50]
mean = sum(data) / len(data)
#print("Mean:", mean)

median = len(data) // 2
if len(data) % 2 == 0:
    median = (data[median - 1] + data[median]) / 2
else:
    median = data[median]
#print("Median:", median)

mode = max(set(data), key=data.count)
#print("Mode:", mode)

variance = sum((x-mean) ** 2 for x in data) / len(data)
#print("Variance:", variance)

std = variance ** 0.5
print("Standard Deviation:", std)