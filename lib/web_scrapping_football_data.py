# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 16:45:15 2022

@author: louis
"""
import sys
sys.path.insert(0, r'C:\Users\louis\Desktop\STAT 4243\STAT 4243 Project 5')

from time import sleep
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import web_scrapping_extractor as extractor
import data_cleaner as cleaner

def scrape_transfermarkt(path,url_file):
    xfer_data = pd.DataFrame()
    
    for i in range(22):
        
        browser = webdriver.Firefox(executable_path=path)
        browser.get(url_file[i].strip('\n'))
        html = browser.page_source
        season_data = extractor.extract_xfer_stats(html)
        
        xfer_data = xfer_data.append(season_data)
        sleep(3)
        browser.close()
        
    xfer_data.to_csv("xfer_data.csv")
    
    return

def scrape_fbref(path,url_file):
    
    years = ["2021-22","2020-21","2019-20","2018-19","2017-18","2016-17",
         "2015-16","2014-15","2013-14","2012-13","2011-12","2010-11","2009-10",
         "2008-09","2007-08","2006-07","2005-06","2004-05","2003-04","2002-03",
         "2001-02","2000-01"]
    
    post_2017_data = pd.DataFrame()
    pre_2017_data = pd.DataFrame()
    
    for i in range(22):
        browser = webdriver.Firefox(executable_path=path)
        browser.get(url_file[i].strip('\n'))
        html = browser.page_source
        
        
        season = [years[i] for j in range(20)]
        
        if i<5:
            curr_df = extractor.extract_all_stats(html)
            curr_df.insert(0,'Season',season)
            post_2017_data = post_2017_data.append(curr_df)
        else: 
            curr_df = extractor.extract_some_stats(html)
            curr_df.insert(0,'Season',season)
            pre_2017_data = pre_2017_data.append(curr_df)
        
        print(season[0],'done')
        sleep(3)
        browser.close()
    
        if i==4:
            post_2017_data.to_csv("post_2017_fbref_data.csv")
            
    pre_2017_data.to_csv("pre_2017_fbref_data.csv")
    
    return 

def web_scrape():
    
    path =r'C:\Users\louis\Downloads\geckodriver-v0.32.0-win32(1)\geckodriver.exe'
    xfer_urls = extractor.read_urls('xfer_urls.txt')
    fbref_urls = extractor.read_urls('fbref_urls.txt')
    
    xfer_mkt_df = scrape_transfermarkt(path,xfer_urls)
    fbref_df = scrape_fbref(path,fbref_urls)
    
    cleaner.clean_annual_wages()
    
    return 

web_scrape()