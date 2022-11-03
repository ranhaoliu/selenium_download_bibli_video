from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import json
import requests
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
url='https://api.bilibili.com/x/space/arc/search?mid=37607457&pn=1&ps=25&index=1&order=pubdate&order_avoided=true&jsonp=jsonp'
header = {'user-agent':'Mozilla/5.0'}
r = requests.get(url, headers=header)
status = r.status_code
bvidList = []
if( 200 == status ):
    contentDir = json.loads(r._content)
    vlist = contentDir.get('data').get('list').get('vlist')
    print(vlist)
    for item in vlist:
        bvidList.append(item['bvid'])

for bvid in bvidList:
    # 对指定的url发起请求
    bor.get('https://www.bilibili.com/video/'+bvid+'/?spm_id_from=333.1007.tianma.4-3-11.click')
    sleep(2)
    # WebElement bilibiliHelperHost = bor.findElementByTagName("bilibili-helper-host")
    js = "document.getElementById('bilibili-helper-host').shadowRoot.children[1].children[1].children[4].children[0].children[0].click()"
    res = bor.execute_script(js)
    print("下载完毕")
    # bor.find_element_by_xpath("bilibili-helper-host/html/body/bilibili-helper-host//div/div[2]/ul/li/a").click()
    sleep(10)



# bor.quit()