'''
only for windows
'''

from requests import get
from re import findall
from urllib.request import urlretrieve as urlrt
from zipfile import ZipFile as unzip
import winreg
import os
import sys
import shutil

URL = 'http://chromedriver.storage.googleapis.com/?delimiter=/&prefix='
REG = r'<Prefix>(\d.*?)</Prefix>'
FILE_NAME = 'chromedriver_win32.zip'
FILE_EXE = 'chromedriver.exe'
url_down = 'http://chromedriver.storage.googleapis.com/%schromedriver_win32.zip'


class sd_chrome():
    def __init__(self, _folder=r'./'):
        # 防止文件夹路径不存在
        # 指定下载路径文件夹
        if not os.path.exists(_folder):
            os.makedirs(_folder)

        self.down_folder = _folder

    def getChromeVersion(self):
        # 从注册表获取chrome版本
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Google\Chrome\BLBeacon')
        self.chrome_version = winreg.QueryValueEx(key, 'version')[0]
        return self.chrome_version

    def getChromeDriverVersionList(self):
        # 从网页源代码获取目前提供的版本号
        resp = get(URL)
        self.driver_version = findall(REG, resp.text)  # 返回正则括号中结果的列表
        return self.driver_version

    def compareVersion(self):
        # 版本号的前两部分相等即为匹配
        self.right_version = ''
        chrome_version_list = self.chrome_version.split('.')
        self.driver_version.reverse()
        for ver in self.driver_version:
            _tmp = ver.split('.')
            if chrome_version_list[0] == _tmp[0] and chrome_version_list[1] == _tmp[1]:
                self.right_version = ver
                break
        return self.right_version

    def downloadChromeDriver(self):
        # 下载,为了指定路径必须用urllib库
        if self.right_version != '':
            url_download = url_down % self.right_version
            self.path_file = r'%s\%s' % (self.down_folder, FILE_NAME)
            urlrt(url_download, self.path_file)  # 已测试会自动覆盖
            print('已下载到:%s' % self.path_file)
            return self.path_file
        else:
            print('未获取到版本号,没有下载')

    def unzipFile(self):
        # 解压
        zip = unzip(self.path_file, 'r')
        for file in zip.namelist():
            zip.extract(file, self.down_folder)
        zip.close()
        print('解压成功')
        self.driver_file = r'%s\%s' % (self.down_folder, FILE_EXE)
        return self.driver_file

    def replaceDriverInPython(self):
        isdone = False
        # 替换Python Script文件夹里面的chromedriver
        # 在里面寻找Python路径,要求下级必须有Scripts文件夹,且路径末尾是Python关键字
        pypath = ''
        for path in sys.path:
            if path.split('\\')[-1] == 'Python' and os.path.isdir(path):
                for d in os.listdir(path):
                    if os.path.isdir(os.path.join(path, d)) and d == 'Scripts':
                        pypath = '%s\\%s' % (path, d)
                        break
            if pypath != '':
                break

        if pypath != '':
            dst_path = '%s\\%s' % (pypath, FILE_EXE)
            if os.path.isfile(dst_path):
                os.remove(dst_path)
            shutil.move(self.driver_file, pypath)
            isdone = True
        else:
            isdone = False

        return isdone


if __name__ == '__main__':
    down = r'./'
    goo = sd_chrome(down)
    a = goo.getChromeVersion()
    b = goo.getChromeDriverVersionList()
    c = goo.compareVersion()
    d = goo.downloadChromeDriver()
    e = goo.unzipFile()
    f = goo.replaceDriverInPython()
