file1 = 'facebook_dinosaur_speed_file1.txt'
file2 = 'facebook_dinosaur_speed_file2.txt'

import pandas as pd
def speed_rank(file1, file2):
  speed={}
  df1 = pd.read_csv(file1, index_col='name')
  df2 = pd.read_csv(file2, index_col='animal')
  for item in df1.index: 
    if item in df2.index and df1.loc[item]['type'] == 'animal':
      speed[item] = df1.loc[item]['leg_length'] * df2.loc[item]['stride'] / df1.loc[item]['weight']
  speed_list = sorted(speed.items(), key = lambda x:x[1], reverse=True)
  return [x[0] for x in speed_list]
print(speed_rank(file1, file2))
