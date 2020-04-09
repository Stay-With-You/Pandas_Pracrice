'''
import pandas as pd
import numpy as np

# 通过numpy数组创建Series
# pd.Series(np.arange(4,10))
# pd.Series([11,12,14], index=['北京','上海','广州'])

#创建一个3行4列的Dataframe数据
data_3_4 = pd.DataFrame(np.arange(10,22).reshape(3,4))
#打印第一行数据
# data_3_4[:1]
#打印第一列数据
# data_3_4[:][0]

#读取
#data = pd.read_csv('pandas_open.csv')
#去除控制
#data.dropna()
'''

import pandas as pd
import numpy as np
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


# 1. Create df with labels as index
	# index索引的用途：
	 # 1.更方便的数据查询
	 # 2.使用index可以获得性能的提升
	 # 3.自动的数据对齐功能（pandas的强大特性）
	 # 4.更多更强大的数据结构支持
df = pd.DataFrame(data, index = list(labels))  # change the index with the lables

# 2. Show df basic information and its data
print(df)  # check the answer of the change and print them on the screen.
print("\n")

# 3. Select only the 'animal' and 'age' columns
# loc是根据属性名进行索引，而iloc则是根据列号进行索引，
#    如df.loc[:, ‘u’]和df.iloc[:, 0]实现的是相同的功能
col01 = df.loc[:, ['animal', 'age']]
# or: col01 = df[['animal', 'age']]
print(col01)
print("\n")

# 4. Select the row with missing value.
row01 = df.loc['d']
row02 = df.loc['h']
print("row01:\n", row01)
print("row02:\n", row02)
print("\n")

# 5. Sort DF in descending age and ascending visits order
print("Descending Order by Visits:")
desc_sort = df.sort_values(by = "visits", ascending = False)
print(desc_sort)
print("\n")
print("Ascending Order by Visits:")
asc_sort = df.sort_values(by = "visits", ascending = True)
print(asc_sort)
print("\n")

# 6. In the 'animal' column, replace 'Snake' with 'Python'
df.loc['c', 'animal'] = 'Python'
df.loc['g', 'animal'] = 'Python'
print("After Change:")
print(df)

