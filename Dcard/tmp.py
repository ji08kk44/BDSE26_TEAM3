from random import uniform
from time import sleep
import os
import json

from fake_useragent import UserAgent
import cloudscraper

from datetime import timezone, datetime
import dateutil.parser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

file_num = 2



end = file_num
Flag = 1


path_list = sorted(os.listdir(r".\Dcard_article_id")[file_num-1: end])
for file_name in path_list:
    data_length = 0
    if os.path.exists(f"Dcard_data\{file_name.split('.')[0]}.json"):
        json_file = open(f"Dcard_data\{file_name.split('.')[0]}.json", 'r', encoding = "utf-8")
        data = json.load(json_file)
        data = data[0:-1]
        data_leangth = len(data)
    file = open(f"Dcard_article_id\{file_name}", 'r', encoding = "utf-8")
    print(f"{file_name} start")
    total_id = len(file.readlines())
    file.seek(0,0)
    for index,line in enumerate(file.readlines())[len(data_leangth):]:
        article_id = line.strip("\n")
        print(article_id)


path_list = sorted(os.listdir(r".\Dcard_article_id")[file_num-1: end])
file = open(f"Dcard_article_id\{234862780}.txt", 'r', encoding = "utf-8")
for index,line in enumerate(file.readlines()[60:]):
    article_id = line.strip("\n")
    print(article_id)
