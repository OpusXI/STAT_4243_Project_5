# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 13:00:12 2022

@author: louis
"""


import sys
sys.path.insert(0, r'C:\Users\louis\Desktop\STAT 4243\STAT 4243 Project 5')

import pandas as pd
import data_cleaner as cleaner

path = ""

overall = pd.read_csv(path+"overall_stats.csv")
passing = pd.read_csv(path+"passing.csv")
possession = pd.read_csv(path+"possession.csv")
defending = pd.read_csv(path+"defending.csv")
shooting = pd.read_csv(path+"shooting.csv")
wages = pd.read_csv(path+"wages.csv")
goalkeep = pd.read_csv(path+"goalkeeping.csv")


overall = overall.rename(columns=overall.iloc[0])
overall = overall.iloc[1:,:]
overall = overall[['Player','Squad','Pos','xG']].iloc[:,:-1]

passing = passing.rename(columns=passing.iloc[0])
passing = passing.iloc[1:,:13]
passing = passing[['Player','Squad','Cmp','Att','Cmp%','TotDist','PrgDist']]

possession = possession.rename(columns=possession.iloc[0])
possession = possession.iloc[1:,]
possession = possession[['Player','Squad','Succ','Att']]

defending = defending.rename(columns=defending.iloc[0])
defending = defending.iloc[2:,]
defending = defending[['Player','Squad','Tkl','TklW','Def 3rd','Mid 3rd','Att 3rd',
                     'Blocks','Int','Clr','Err']]
defending = pd.merge(defending.iloc[:,:3],defending.iloc[:,4:],left_index=True,right_index=True)

shooting = shooting.rename(columns=shooting.iloc[0])
shooting = shooting.iloc[1:,]
shooting = shooting[['Player','Squad','Sh','SoT','SoT%','xG']]

temp_1 = pd.merge(overall,passing,on=['Player','Squad'])
temp_2 = pd.merge(possession,defending,on=['Player','Squad'])
master = pd.merge(temp_1,shooting,on=['Player','Squad'])
master = pd.merge(master,temp_2,on=['Player','Squad'])

master = master.dropna(subset=['Pos'])
positions = []
for pos in master['Pos']:
    
    positions.append(pos[0:2])
    
master['Pos'] = positions
master = master.fillna(0)


wages = wages[['Player','Squad','Annual Wages']]

clean_wages = []
for wage in wages['Annual Wages']:
    clean_wages.append(float(wage.split(" ")[1]))
wages['Annual Wages']=clean_wages

master = pd.merge(master,wages,on=['Player','Squad'])

#print(len(master))

goalkeep = goalkeep.rename(columns=goalkeep.iloc[0])
goalkeep = goalkeep[['Player','Squad','PSxG']]

master = pd.merge(master,goalkeep,on=['Player','Squad'],how="outer")
master.fillna(0,inplace=True)

master.drop(master.index[533:],inplace=True)

master.to_csv("player_stats.csv")




# We are not standardizing the stats to per 90min because we are not accounting
# for injuries and rotational players. We want consistent results.