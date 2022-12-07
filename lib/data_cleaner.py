# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 22:25:02 2022

@author: louis
"""


def clean_year(year_list):
 
    for i in range(len(year_list)):
        year = year_list[i].split('/')
        year_list[i] = "20" + year[0] + "-" + year[1]
    
    return year_list
        
    
def clean_expenditure(money):

    for i in range(len(money)):
        if money[i] == '-':
            money[i] = 0
        else:            
            if money[i][-1] == 'm':
                money[i]=float(money[i][1:-1])*1000000
            else:
                money[i]=float(money[i][1:-1])*1000
                
    return money
    
def clean_squad_names(squads):
    
    for i in range(len(squads)):
        squads[i] = squads[i].replace("RCD Espanyol Barcelona","Espanyol")
        squads[i] = squads[i].replace("Real Oviedo","Oviedo")
        squads[i] = squads[i].replace("Real Betis Balompié","Betis")
        squads[i] = squads[i].replace("Albacete Balompié","Albacete")
        squads[i] = squads[i].replace("Bilbao","Club")
        squads[i] = squads[i].replace(" de Tarragona","")
        squads[i] = squads[i].replace("Racing Santander","Racing Sant")
        squads[i] = squads[i].replace("Real Zaragoza","Zaragoza")
        squads[i] = squads[i].replace("Real Valladolid","Valladolid")
        squads[i] = squads[i].replace("RCD ","")
        squads[i] = squads[i].replace("de ","")
        squads[i] = squads[i].replace(" FC","")
        squads[i] = squads[i].replace("FC ","")
        squads[i] = squads[i].replace(" CF","")
        squads[i] = squads[i].replace("CF ","")
        squads[i] = squads[i].replace(" CD","")
        squads[i] = squads[i].replace("CD ","")
        squads[i] = squads[i].replace("UD ","")
        squads[i] = squads[i].replace(" UD","")
        squads[i] = squads[i].replace("SD ","")
        squads[i] = squads[i].replace("CA ","")
        squads[i] = squads[i].replace("Deportivo ","")
        squads[i] = squads[i].replace(" Huelva","")
    
    return squads

def clean_annual_wages():
    
    years = [2017,2018,2019,2020,2021]

    annual_wages = pd.DataFrame()
    for year in years:
        f = "wage_{}.csv".format(str(year))
        season = [str(year)+"-"+str(year+1)[2:]]
        
        wage = pd.read_csv(f)
        season = season*len(wage)
        
        wage['Season'] = season
        annual_wages = annual_wages.append(wage)
        
    new_wages = []    
    for wage in annual_wages['Annual Wages']:
        new_wages.append(int(wage.split(" ")[1]))
        
    annual_wages['Annual Wages']=new_wages
    annual_wages = annual_wages[['Season','Rk','Squad','Annual Wages']]
    annual_wages.to_csv("annual_wages_by_team.csv")
    
    return
