import requests
from jsonpath import JSONPath
from datetime import datetime
#这里的cookie需要自己去抓取 看redme教程
cookies = {
    #这里copy spidertools 中的cookie代码块
    
}

headers = {
    'Host': 'cloud.h2os.com',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'Accept': 'application/json, text/plain, */*',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://cloud.h2os.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://cloud.h2os.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_uab_collina=170139669235676977952667; opcloud_token=HT_nNg6EdV-KHOcxEcJX8CD3GcwsZ2Zh09CYy3wZ6b-BXrGdWVhRVR_4XVBYPT2KHgn0NUR8E2AGIFZQMYJKXEWvw5PV-3qko7xT91m1GPysEEatNKHIbFjgw; NEARME_ACCOUNTNAME_COOKIE=WearingCucumber; accountName=WearingCucumber; opcloud_sid=c533fb6381b24659bc077327cd043375; opcloud_vcode=4ffd6e7ced094e29b4613b0563161369',
}

data = {
    'size': '100',
    'state': 'active',
    'smallPhotoScaleParams': 'image/resize,m_mfit,h_250,w_250',
    'originalPhotoScaleParams': 'image/resize,m_mfit,h_1300,w_1300',
    'cursor': str(datetime.now()).split(' ')[0].replace('-',''),
}

response = requests.post('https://cloud.h2os.com/gallery/pc/listNormalPhotos', cookies=cookies, headers=headers, data=data,verify=False).json()
lastDay = response['lastMatchedMoment']
startDay = response['startTime']
photoUrls = JSONPath("$.photos..originalPhotoUrl").parse(response)
url_lst = []
url_lst.extend(photoUrls)

while True:
    if lastDay != startDay:
        data['cursor'] = lastDay
        response = requests.post('https://cloud.h2os.com/gallery/pc/listNormalPhotos', cookies=cookies, headers=headers, data=data,verify=False).json()
        lastDay = response['lastMatchedMoment']
        photoUrls = JSONPath("$.photos..originalPhotoUrl").parse(response)
        url_lst.extend(photoUrls)
        print(lastDay)
    else:
        break
#这里将抓取的url保存到photoUrls.txt
with open('photoUrls.txt', 'w+', encoding='utf8')as f:
    f.write(str(url_lst))
