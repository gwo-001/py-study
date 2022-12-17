import urllib.request


def firstRequest():
    response = urllib.request.urlopen('https://www.baidu.com/')
    print(response.read().decode('utf-8'))

"""
抖音热榜请求
"""
def douYingHotList():
    douYingHotListDomain = "https://www.douyin.com/aweme/v1/web/hot/search/list/"
    request.urlopen(douYingHotListDomain+'?%s')