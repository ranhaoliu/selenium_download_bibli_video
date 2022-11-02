from selenium import webdriver
from time import sleep
extension_path="./bilibili-helper-2.1.7.crx"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension(extension_path)
chrome_options.add_argument(r'user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data')
chrome_options.add_experimental_option('useAutomationExtension', False)
# 禁止下载弹窗

prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'D:\\'}
chrome_options.add_experimental_option('prefs', prefs)
# 实例化一款浏览器
bor = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)

# 对指定的url发起请求
bor.get('https://www.bilibili.com/video/BV1a8411Y7Go/?spm_id_from=333.1007.tianma.4-3-11.click')
sleep(10)
# WebElement bilibiliHelperHost = bor.findElementByTagName("bilibili-helper-host")
js = "document.getElementById('bilibili-helper-host').shadowRoot.children[1].children[1].children[4].children[0].children[0].click()"
res = bor.execute_script(js)

# bor.find_element_by_xpath("bilibili-helper-host/html/body/bilibili-helper-host//div/div[2]/ul/li/a").click()

sleep(20000)



# bor.quit()