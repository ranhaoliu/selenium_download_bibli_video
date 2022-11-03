import json

import requests

url="https://api.bilibili.com/x/space/arc/search?mid=470292848&ps=30&tid=0&pn=1&keyword=&order=pubdate&order_avoided=true&jsonp=jsonp"
# url='https://api.bilibili.com/x/space/arc/search?mid=37607457&pn=1&ps=25&index=1&order=pubdate&order_avoided=true&jsonp=jsonp'
header = {'user-agent':'Mozilla/5.0'}
r = requests.get(url, headers=header)
status = r.status_code
bvid = []
if( 200 == status ):
    contentDir = json.loads(r._content)
    vlist = contentDir.get('data').get('list').get('vlist')
    print(vlist)
    for item in vlist:
        bvid.append(item['bvid'])
    print("111111111111")


