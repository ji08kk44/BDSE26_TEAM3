from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
import requests as req
from bs4 import BeautifulSoup as bs
import json

# ptt的某個網頁
url = 'https://www.ptt.cc/bbs/Stock/index5240.html'



my_options = webdriver.ChromeOptions()
# 不要開啟瀏覽器
my_options.add_argument("--headless")

browser = webdriver.Chrome(
    options = my_options,
    service = Service(ChromeDriverManager().install())
)



listData = []
artData = []
url_list = []
article_list = []

browser.get(url)


# 想要的日期
def search_date(year_num, month_num, date_num):
    year = str(year_num)
    month = str(month_num)
    date = str(date_num)
    date_list = []
    date_index = []
    url_index = []
    
    if len(date) == 1:
        date = '0' + date
        want_date = month + '/' + date
        date = browser.find_elements(By.CSS_SELECTOR,"div.r-ent div.meta div.date")
        
    # 找出網址中所有文章的日期
    for i in date:
        date_list.append(i.text)
        
    # 找出想要的日期位置
    for index, char in enumerate(date_list):
        if char == want_date:
            date_index.append(index)
    
    # 一篇一篇文章找
    for i in date_index:
        a = browser.find_elements(By.CSS_SELECTOR,"div.r-ent div.title a")[i]
        
        # 標題
        title_list = a.text
        
        # 文章網址
        aLink = a.get_attribute('href')
        url_list.append(aLink)     
        listData.append({
                 "日期": want_date,
                 "標題": title_list,
                 "網址": aLink
        })
    year = str(year)
        
    comment_list = [[] for i in range(len(url_list))]
    for art in range(len(url_list)):
        reqs = req.get(url_list[art])
        soup = bs(reqs.text,'lxml')
        
        for a in soup.select('div.bbs-screen.bbs-content'):
            content = str(a.get_text)
            top = content.index(year+'</span></div>')
            bot = content.index('※')
            article = content[top+17:bot-20]
            final =(article.replace('\n', " "))
            article_list.append({
                '文章內容': final
            })


        for commnt in soup.select('div.push'):
            comment = commnt.get_text()
            comment_list[art].append(comment)
            
            
    for i in range(len(listData)):
        listData[i].update(
            article_list[i]
            )
        listData[i].update({
            "留言":comment_list[i]
            })     


def downlaod_json(day):
    file = f'{day}_stock.json'
    with open(file, 'w',encoding = 'utf-8') as flObj:
        json.dump(listData,flObj, ensure_ascii=False, indent=4)
        print('成功')



search_date(2022,7,1)
downlaod_json(20220701)




