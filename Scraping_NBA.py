#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 15:31:39 2018

@author: garyliu
"""
import os
os.getcwd()
os.chdir("/Users/garyliu/Documents/GitHub/course-programming-for-ds-Quiz")

from bs4 import BeautifulSoup as bs
import requests
import bs4
import pandas as pd
import numpy as np

url = "https://www.basketball-reference.com/teams/GSW/2019.html"
res = requests.get(url)
soup = bs(res.text)
roster = soup.findAll("table", {"id":"roster"})[0].findAll("tbody")
player_personal = roster[0].findAll("tr")
player_detail = player_personal[0].findAll("td")
for i in range(len(player_personal)):
    for j in range(len())
    player_personal[i]



data = np.array([[1,2,3], [2,3,4], [5,6,7]])
df = pd.DataFrame(data = data)

