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
        'device_platform': 'webapp',
        'aid': '6383',
        'channel': 'channel_pc_web',
        'detail_list': '1',
        'source': '6',
        'pc_client_type': '1',
        'version_code': '170400',
        'version_name': '17.4.0',
        'cookie_enabled': 'true',
        'screen_width': 1537,
        'screen_height': 864,
        'browser_language': 'zh-CN',
        'browser_platform': 'Win32',
        'browser_name': 'Chrome',
        'browser_version': '108.0.0.0',
        'browser_online': 'true',
        'engine_name': 'Blink',
        'engine_version': '108.0.0.0',
        'os_name': 'Windows',
        'os_version': 10,
        'cpu_core_num': 8,
        'device_memory': 8,
        'platform': 'PC',
        'downlink': 10,
        'effective_type': '4g',
        'round_trip_time': '50',
        'webid': 7178048266700293636,
        'msToken': 'ZS9JQ-cb_iJchss8Zx1FMWlELQwHn43xE76CQdgC7nxGH6LE78snFxE0g_pWdh5Wdi4UCEwc0WDAjlzEu8W2PqojizbWSJ'
                   '-uKT4uq9kwBgRlgI2ft_91-y-c9w-xGM8JuQ==',
        'X-Bogus': 'DFSzswVu39zANJZZSdOupRXAIQ5q'
    }
    resp = urllib.request.urlopen(Url_request_for_get(douYingHotListDomain, params).BuildUrlWithParams())
    return resp.read().decode('utf-8')
