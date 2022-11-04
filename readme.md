#项目背景
最近我想把自己在哔哩哔哩上发的视频全部下载下来，发现哔哩哔哩网页版没有下载功能，app客户端只能一个一个缓存，
然后我找到网上的一些教程，发现大多数都是让我去下载一些客户端的软件，我不想用，最后发现一个chrome插件bilibili-helper-2.1.7.crx
可以帮我一个一个下载，但它不能满足我一下子下载的全部视频的功能，然后，我思考了片刻，
决定利用这个插件加上我所学的自动化测试框架，简单写一些代码，尝试完成这个批量下载某个up主的全部视频的功能，
于是就有了这个项目，虽然它很小，而且是寄生在bilibili-helper-2.1.7.crx插件之上的，但不得不说它确实解决了
我当下的小问题。
## 使用说明: 
1.先运行 LoadChromeDriver.py 会自动下载与你浏览器匹配的chromedriver <br/>
2.再运行LoadExtensionPlug.py 文件输入up主的mid <br/>
mid 是每个up主的唯一id，例如up主老番茄的主页url为: https://space.bilibili.com/546195/，那么后面的数字546195即是老番茄的 mid<br/>
3.然后生成的视频会在你的 D:\\myVideo\\ 文件夹下，如果你没有D盘，请更改代码里的path变量，当然你也可以改为其他<br/>
4.使用前请关掉你的浏览器，不然会报错，这是一个bug，如果下载失败，请清空一下浏览器的缓存
### 我用的浏览器版本如下
版本 107.0.5304.88（正式版本） （64 位）
如果你使用的是其他版本的浏览器，请如 [chromedriver 下载站点](https://registry.npmmirror.com/binary.html?path=chromedriver/)下载与浏览器版本对应的chromedriver
你可以运行 本项目中的LoadChromeDriver.py 自动帮你下载和你浏览器匹配的chromedriver，但你事先必须安装chrome浏览器
### 参考
1.[bilibili-helper 下载地址](https://csser.top/)<br/>
2.[使用selenium 加载chrome插件](https://blog.csdn.net/CY19980216/article/details/120808137)<br/>
3.[selenium 下载文件时 出现保存弹窗让选路径，下载被卡主问题](在一个外国的网站找的解决方案，网了地址了)<br/>
4.[Web自动化遇到shadowDOM节点操作](https://blog.csdn.net/weixin_53519100/article/details/114760056?spm=1001.2101.3001.6650.8&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EESLANDING%7Edefault-8-114760056-blog-101566770.pc_relevant_landingrelevant&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EESLANDING%7Edefault-8-114760056-blog-101566770.pc_relevant_landingrelevant&utm_relevant_index=9)<br/>
5.[selenium 获取shadow-root的元素](https://blog.csdn.net/dyfDewey/article/details/116454716?spm=1001.2101.3001.6650.8&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-8-116454716-blog-119808566.pc_relevant_3mothn_strategy_recovery&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-8-116454716-blog-119808566.pc_relevant_3mothn_strategy_recovery&utm_relevant_index=12)<br/>
6.[自动下载与用户浏览器匹配的ChromeDriver](https://blog.csdn.net/sinat_41870148/article/details/109263847)<br/>
### 我的 
[我的博客](https://blog.csdn.net/weixin_43225966)
[github链接](https://github.com/ranhaoliu/selenium_download_bibli_video)

