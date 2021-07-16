# coding=utf-8
import requests
from bs4 import BeautifulSoup
import csv
import random, time


url_A = 'https://www.istockphoto.com/search/2/image?page='
url_B = '&phrase=Beef'
headers = {
    "Referer": "https://www.istockphoto.com/search/2/image?",
}

all_job_datas = []
for page in range(1, 5 + 1):
    url = url_A + str(page) + url_B
    print(url)
    htmlFile = requests.get(url)
    ObjSoup = BeautifulSoup(htmlFile.text, 'html.parser')
    jobs = ObjSoup.find_all('article', class_='MosiacAsset-module__container___1bO9p')  # 搜尋所有職缺

    for job in jobs:
        job_name = job.find('figcaption', class_="MosiacAsset-module__figcaption___AKIMK").text  # 內容
        job_url = job.find('img').get('src')  # 網址
        job_data = {'圖片內容': job_name, '網址': job_url}
        all_job_datas.append(job_data)
    time.sleep(random.randint(1, 3))

fn = '牛排.csv'  # 取CSV檔名
columns_name = ['圖片內容', '網址']  # 第一欄的名稱
with open(fn, 'w', newline='', encoding="utf_8_sig") as csvFile:  # 定義CSV的寫入檔,並且每次寫入完會換下一行
    dictWriter = csv.DictWriter(csvFile, fieldnames=columns_name)  # 定義寫入器
    dictWriter.writeheader()
    for data in all_job_datas:
        dictWriter.writerow(data)

