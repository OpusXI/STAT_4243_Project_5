# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 20:51:54 2022

@author: louis
"""
import sys
sys.path.insert(0, r'C:\Users\louis\Desktop\STAT 4243\STAT 4243 Project 5')

from time import sleep
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import data_cleaner as cleaner


def read_urls(file_name):
    
    path = r'C:\Users\louis\Desktop\STAT 4243\STAT 4243 Project 5\{}'.format(file_name)
    
    with open(path) as f:
        urls = f.readlines()
        f.close()
    
    return urls

def extract_overall(soup):
    ranks, teams, wins, draws, losses, goals_for, goals_against = [], [], [], [], [], [], []
    goals_diff, points, avg_points, x_goals, x_goals_against, x_goals_diff = [], [], [], [], [], []
    
    for i in range(20):
        curr_team = soup.find_all('tr',{"data-row": str(i)})[0]
        data = curr_team.select('td')
        
        ranks.append(i+1)
        teams.append(data[0].text.strip())
        wins.append(float(data[2].text.strip()))
        draws.append(float(data[3].text.strip()))
        losses.append(float(data[4].text.strip()))
        goals_for.append(float(data[5].text.strip()))
        goals_against.append(float(data[6].text.strip()))
        goals_diff.append(float(data[7].text.strip()))
        points.append(float(data[8].text.strip()))
        avg_points.append(float(data[9].text.strip()))
        x_goals.append(float(data[10].text.strip()))
        x_goals_against.append(float(data[11].text.strip()))
        x_goals_diff.append(float(data[12].text.strip()))
        
    d = {'rank':ranks,'team':teams, 'wins':wins, 'draws':draws, 'losses':losses,'goals_for':goals_for,
         'goals_against':goals_against,'goals_diff':goals_diff,'points':points,
         'avg_points':avg_points, 'x_goals':x_goals,'x_goals_against':x_goals_against,
         'x_goals_diff':x_goals_diff}
    
    overall = pd.DataFrame(d)
    
    return overall

def extract_details(soup):
    team, shots, SoT, SoT_p = [], [], [], []
    cmp_pass, att_pass, cmp_pass_p, total_dist_pass, prg_dist_pass = [],[], [], [], []
    tackles, tackles_w, block_s, block_p, intercepts, clearance, errors = [], [], [], [], [], [], []
    d_tackles, m_tackles, a_tackles = [], [], []
    poss, succ_dribble, att_dribble = [], [], []
    
    for i in range(20):
        curr_team = soup.find_all('tr',{"data-row": str(i)})[8]
        data = curr_team.select('td')
        team.append(curr_team.select('a')[0].text)
        shots.append(float(data[3].text))
        SoT.append(float(data[4].text))
        SoT_p.append(float(data[5].text))
        
        
        curr_team = soup.find_all('tr',{"data-row": str(i)})[10]
        data = curr_team.select('td')
        cmp_pass.append(float(data[2].text))
        att_pass.append(float(data[3].text))
        cmp_pass_p.append(float(data[4].text))
        total_dist_pass.append(float(data[5].text))
        prg_dist_pass.append(float(data[6].text))
        
        
        curr_team = soup.find_all('tr',{"data-row": str(i)})[16]
        data = curr_team.select('td')
        tackles.append(float(data[2].text))
        tackles_w.append(float(data[3].text))
        d_tackles.append(float(data[4].text))
        m_tackles.append(float(data[5].text))
        a_tackles.append(float(data[6].text))
        block_s.append(float(data[12].text))
        block_p.append(float(data[13].text))
        intercepts.append(float(data[14].text))
        clearance.append(float(data[16].text))
        errors.append(float(data[17].text))
        
        
        curr_team = soup.find_all('tr',{"data-row": str(i)})[18]
        data = curr_team.select('td')
        poss.append(float(data[1].text))
        succ_dribble.append(float(data[10].text))
        att_dribble.append(float(data[11].text))
        
    d = {'team':team, 'shots':shots, 'SoT':SoT, 'SoT_p':SoT_p, 'cmp_pass':cmp_pass,
         'att_pass':att_pass, 'cmp_pass_p':cmp_pass_p, 'total_dist_pass':total_dist_pass,
         'prg_dist_pass':prg_dist_pass, 'tackles':tackles, 'tackles_w':tackles_w, 'd_tackles':d_tackles,
         'm_tackles':m_tackles, 'a_tackles':a_tackles,
         'block_s':block_s, 'block_p':block_p, 'intercepts':intercepts, 'clearance':clearance,
         'errors':errors, 'poss':poss, 'succ_dribble':succ_dribble, 'att_dribble':att_dribble}
    
    detail = pd.DataFrame(d)
    
    return detail

def extract_all_stats(html):
    soup = BeautifulSoup(html, 'html5lib')
    overall = extract_overall(soup)
    details = extract_details(soup)
    results = pd.merge(overall,details,on='team')

    return results

def extract_some_overall(soup):
    ranks, teams, wins, draws, losses, goals_for, goals_against = [], [], [], [], [], [], []
    goals_diff, points, avg_points= [], [], []
    
    for i in range(20):
        curr_team = soup.find_all('tr',{"data-row": str(i)})[0]
        data = curr_team.select('td')
        
        ranks.append(i+1)
        teams.append(data[0].text.strip())
        wins.append(float(data[2].text.strip()))
        draws.append(float(data[3].text.strip()))
        losses.append(float(data[4].text.strip()))
        goals_for.append(float(data[5].text.strip()))
        goals_against.append(float(data[6].text.strip()))
        goals_diff.append(float(data[7].text.strip()))
        points.append(float(data[8].text.strip()))
        avg_points.append(float(data[9].text.strip()))

        
    d = {'rank':ranks,'team':teams, 'wins':wins, 'draws':draws, 'losses':losses,'goals_for':goals_for,
         'goals_against':goals_against,'goals_diff':goals_diff,'points':points,
         'avg_points':avg_points}
    
    overall = pd.DataFrame(d)
    
    return overall

def extract_some_detail(soup):
    team, SoT = [], []
    
    for i in range(20):
        curr_team = soup.find_all('tr',{"data-row": str(i)})[6]
        data = curr_team.select('td')
        team.append(curr_team.select('a')[0].text)
        SoT.append(float(data[4].text))

    d = {'team':team, 'SoT':SoT}
    
    detail = pd.DataFrame(d)
    
    return detail
    
def extract_some_stats(html):
    soup = BeautifulSoup(html, 'html5lib')
    overall = extract_some_overall(soup)
    details = extract_some_detail(soup)    
    results = pd.merge(overall,details,on='team')
    
    return results

def extract_xfer_stats(html):
    soup = BeautifulSoup(html, 'html5lib')
    
    team, year, expenditure = [], [], []

    for i in range(10):
        data = soup.select('tr.odd')[i].select('td')
        team.append(data[2].text.strip())
        year.append(data[3].text.strip())
        expenditure.append(data[4].text.strip())
        
        data = soup.select('tr.even')[i].select('td')
        team.append(data[2].text.strip())
        year.append(data[3].text.strip())
        expenditure.append(data[4].text.strip())
        
    year = cleaner.clean_year(year)
    expenditure = cleaner.clean_expenditure(expenditure)
    team = cleaner.clean_squad_names(team)
    
    d = {'team':team, 'Season':year, 'expenditure':expenditure}
    
    result = pd.DataFrame(d).sort_values('expenditure')
    print(year[0], 'done')
    
    return result