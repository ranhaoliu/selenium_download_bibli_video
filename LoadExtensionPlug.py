from selenium import webdriver
from time import sleep

extension_path="./bilibili-helper-2.1.7.crx"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension(extension_path)
chrome_options.add_argument(r'user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data')
chrome_options.add_experimental_option('useAutomationExtension', False)
# 实例化一款浏览器
bor = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)

# 对指定的url发起请求
bor.get('https://www.bilibili.com/video/BV1a8411Y7Go/?spm_id_from=333.1007.tianma.4-3-11.click')

sleep(20000)



# bor.quit()