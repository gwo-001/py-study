import urllib.request

from spider.dtos.UrlHelperDtos import Url_request_for_get


def firstRequest():
    response = urllib.request.urlopen('https://www.baidu.com/')
    print(response.read().decode('utf-8'))


"""
抖音热榜请求
"""


def douYingHotList():
    douYingHotListDomain = "https://www.douyin.com/aweme/v1/web/hot/search/list/"
    params = {
        'count': 10,
        'Seo-Flag': 0,
        'channel_id': 99,
        'pc_client_type': 1,
        'version_name': '17.4.0'
    }
    resp = urllib.request(Url_request_for_get(douYingHotListDomain, params).BuildUrlWithParams())
    return resp.read().decode('utf-8')
