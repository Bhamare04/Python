# # import matplotlib.pyplot as plt
# # hours = [3,2,4,1,2,5]
# # scores = [10,4,5,2,98,76]
# # plt.scatter(hours,scores)
# # plt.xlabel('Hours Studied')
# # plt.ylabel('Test Scores')
# # plt.title('Scatter Plot of Hours Studied vs Test Scores')
# # plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# del df['species']
# #correlation matrix
# correlation = df.corr()

# #plotting the heatmap
# sns.heatmap(correlation,annot= True,cmap='coolwarm')
# plt.title('Correlation Heatmap of Iris Dataset')
# plt.show()

# #matlpotlib subplots
# fig, axes = plt.subplots(2, 2, figsize=(10, 10))
