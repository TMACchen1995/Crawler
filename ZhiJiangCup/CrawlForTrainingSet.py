import os
import re
import requests
import json
from bs4 import BeautifulSoup as bs
import pandas as pd

root = 'https://www.shutterstock.com/search/'
filename = './coco.names'

def get_pathes(root, file_name):
    keywords = [i.strip() for i in open(filename)]
    pathes = [os.path.join(root,i) for i in keywords]
    return pathes

pathes = get_pathes(root, filename)

def crawl(pathes):
    zhijiangcup_trainingset = {}
    for path in pathes:
        response = requests.get(path, headers={'User-Agent': 'Chrome/74.0.3724.8'})
        soup = bs(response.text, 'html.parser')
        content = soup.select('div.z_g_b')

        for element in content:
            pics_link = element.select('img')[0]['src']
            describle = element.select('img')[0]['alt']
            zhijiangcup_trainingset[pics_link] = describle

    return zhijiangcup_trainingset

zhijiangcup_trainingset = crawl(pathes)     #len(zhijiangcup_trainingset)  = 8229

zhijiangcup_trainingset = json.dumps(zhijiangcup_trainingset)

with open('zhijiangcup_trainingset.json', 'w') as f:
    f.write(zhijiangcup_trainingset)
