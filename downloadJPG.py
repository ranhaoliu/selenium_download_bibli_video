# coding:utf-8
import os
import requests
import json
import time
def download(records):
    for record in records:
        ctime = record.get('ctime')
        dir = os.getcwd() + "\\image\\" + ctime + "\\"
        if not os.path.exists(dir):
            os.makedirs(dir)
        urls = record.get('src')
        description = record.get('desc')
        for url in urls:
            r = requests.get(url)
            file_path = os.path.splitext(url)[0]
            file_name = file_path.split('/')[-1]
            with open(dir + file_name + '.jpg', 'wb') as f:
                f.write(r.content)
        # 写文本文件
        with open(dir + '/description.txt', encoding='utf-8', mode='w') as f:
            f.write(str(description))

def getRecords(url):
    r = requests.get(url, headers=header)
    status = r.status_code
    if (200 == status):
        contentDir = json.loads(r._content)
        items = contentDir.get('data').get('items')
        Records = []
        for item in items:
            oneRecord = {}
            description = item.get('description')
            pictures = item.get('pictures')
            timeStamp = item.get('ctime')
            timearr = time.localtime(timeStamp)
            ctime = time.strftime("%Y_%m_%d_%H_%M_%S", timearr)
            srcList = []
            picture_size = len(pictures)
            for picture in pictures:
                src = picture.get('img_src')
                srcList.append(src)
            oneRecord.setdefault('desc', description)
            oneRecord.setdefault('src', srcList)
            oneRecord.setdefault('ctime', ctime)
            Records.append(oneRecord)
    return Records


# uid = '546195'
uid = input("请输入up主的uid,然后按回车键: ")
# 得到总的相薄中动态的总个数
uid_url = 'https://api.bilibili.com/x/dynamic/feed/draw/upload_count?uid=' + uid + '&jsonp=jsonp'
header = {'user-agent': 'Mozilla/5.0'}
count_request = requests.get(uid_url, headers=header)
count_res = json.loads(count_request._content)
count = count_res.get('data').get('all_count')

# 第几页
page_num = 0
while count > 0:
    url = 'https://api.bilibili.com/x/dynamic/feed/draw/doc_list?uid=' + uid + '&page_num=' + str(page_num) + '&page_size=30&biz=all&jsonp=jsonp'
    records = getRecords(url)
    print("第 "+str(page_num)+' 正在下载')
    download(records)
    page_num += 1
    count = count - 30
