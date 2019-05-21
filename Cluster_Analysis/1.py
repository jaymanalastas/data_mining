#Testing if it goes through Git.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\14078\PycharmProjects\Data_Mining\Cluster_Analysis\single_family_home_values.csv")

# print(df.head(10))
# print(type(df))
# print(df.shape) #shows the range of data within the CSV file
# print(df.info())  #Create a summary for the columns. It shows the title and data count
# print(df.describe()) # shows the count, mean, std, min, 25%, 50%, 75% and max


# df2 = df.fillna(0) #fills in missing value for any null with in the CSV file
# print(df2.info())
#
# df3 = df.fillna(df.mean()) #fills null values with mean
# print(df3.info())

df.dropna(inplace = True)
# # print(df.info())
# print(sns.boxplot(df.estimated_value)) #shows a box plot for the estimated_value
# plt.show(block=True)
# df2 = df.fillna('missing')
# print(df2[['estimated_value','yearBuilt','priorSaleAmount']].head(2))
print(df[df.estimated_value<=800000].shape) #creates parameters that prints what we need from the data sets