import pandas as pd

data = pd.read_excel('data/data.xlsx')

for i in range(1, 4):
    x = 'x' + str(i)
    max_ = data[x].max()
    min_ = data[x].min()
    for j in range(len(data[x])):
        new_x = data[x][j]
        data.loc[j, [x]] = (new_x - min_) / (max_ - min_)

max_ = data['d1'].max()
min_ = data['d1'].min()
for i in range(len(data)):
    new_y = data['d1'][i]
    data.loc[i, ['d1']] = (new_y - min_) / (max_ - min_)

data.drop(columns=['Unnamed: 0'], inplace=True)

print(data)

data.to_excel('data/normalized_data.xlsx')
