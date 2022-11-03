from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import json
import requests
from selenium.webdriver.support.wait import WebDriverWait

extension_path="./bilibili-helper-2.1.7.crx"
chrome_options = Options()
chrome_options.add_extension(extension_path)
chrome_options.add_argument(r'user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data')
chrome_options.add_experimental_option('useAutomationExtension', False)
# 禁止下载弹窗

prefs = {'profile.default_content_settings.popups': 0,
        'download.prompt_for_download': False,
         'download.default_directory': 'D:\\myVideo\\',
         "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
         }
chrome_options.add_experimental_option('prefs', prefs)
# 实例化一款浏览器
bor = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)


# 博主的视频
# url = 'https://www.bilibili.com/video/BV1a8411Y7Go/?spm_id_from=333.1007.tianma.4-3-11.click'
#  名字为 凹凸赛克的up博主的首页视频
# url='https://api.bilibili.com/x/space/arc/search?mid=37607457&pn=1&ps=25&index=1&order=pubdate&order_avoided=true&jsonp=jsonp'
# mid="470292848"
# mid="546195"#老番茄
mid = input("请输入up主的mid: ")
url="https://api.bilibili.com/x/space/arc/search?mid="+mid+"&ps=30&tid=0&pn=1&keyword=&order=pubdate&order_avoided=true&jsonp=jsonp"
header = {'user-agent':'Mozilla/5.0'}
r = requests.get(url, headers=header)
status = r.status_code
bvidList = []
if( 200 == status ):
    contentDir = json.loads(r._content)
    vlist = contentDir.get('data').get('list').get('vlist')
    page = contentDir.get('data').get('page')
    ps = page.get('ps')
    count = page.get('count')
    print(vlist)
    for item in vlist:
        bvidList.append(item['bvid'])
    pageCount = 1
    # 遍历列表页，拿到该up主账号下的所有视频bvid
    while count > 0:
        count = count - ps
        if count > 0:
            pageCount += 1
            url = "https://api.bilibili.com/x/space/arc/search?mid=" + mid + "&ps=30&tid=0&pn="+str(pageCount)+"&keyword=&order=pubdate&order_avoided=true&jsonp=jsonp"
            r = requests.get(url, headers=header)
            contentDir = json.loads(r._content)
            vlist = contentDir.get('data').get('list').get('vlist')
            sleep(1) #延时1秒钟
            for item in vlist:
                bvidList.append(item['bvid'])
count = 1
# BV1pJ411Q7vQ
for bvid in bvidList:
    # 对指定的url发起请求
    bor.get('https://www.bilibili.com/video/'+bvid+'/?spm_id_from=333.1007.tianma.4-3-11.click')
    sleep(2)
    # WebElement bilibiliHelperHost = bor.findElementByTagName("bilibili-helper-host")
    js = "document.getElementById('bilibili-helper-host').shadowRoot.children[1].children[1].children[4].children[0].children[0].click()"
    res = bor.execute_script(js)

    # bor.find_element_by_xpath("bilibili-helper-host/html/body/bilibili-helper-host//div/div[2]/ul/li/a").click()
    #  检测页面是否出现下载完成的text，如果出现则进行下一个视频的下载，避免出现还没下载完就跳到新的视频页面
    while True:
        # 记得return 关键字不要忘记
        complete_js = "return document.getElementById('bilibili-helper-host').shadowRoot.children[1].children[1].children[4].children[0].children[2].innerText"
        res = bor.execute_script(complete_js)
        if res == "已下载完成":
            print("视频: " + str(count) + " 下载完毕" + bvid)
            count = count + 1
            break
        sleep(1)

print("该up的所有视频都已经下载完毕")
sleep(100000)

# bor.quit()