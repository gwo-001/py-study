import urllib.request


class Url_request_for_get:

    url = '未知url'
    param = {}
    header = {}

    """
    带了header和参数
    """

    def __init__(self, url, params, header):
        # 0 处理url
        if url is None or len(url) == 0:
            raise Exception("url不能为空")
        if url.endswith('/'):
            self.url = url[:-1]
        else:
            self.url = url
        # 1 处理入参
        if type(params) is dict:
            self.params = params
        else:
            raise Exception('入参不是字典')
        # 2 处理header
        if type(header) is dict:
            self.header = header
        else:
            raise Exception('header不是字典')

    """
    只有参数
    """

    def __init__(self, url, params):
        if url is None or len(url) == 0:
            raise Exception("url不能为空")
        if url.endswith('/'):
            self.url = url[:-1]
        else:
            self.url = url
        if type(params) is dict:
            self.params = params
        else:
            raise Exception('参数不是字典')

    def BuildUrlWithParams(self):
        # 0 处理入参
        if self.params:
            tmpParams = ''
            for k, v in self.params.items():
                tmpParams += str(k) + '=' + str(v) + '&'
            finalUrl = self.url + '?' + tmpParams
            if finalUrl.endswith('&'):
                return finalUrl[:-1]
        return self.url


if __name__ == '__main__':
    douYingHotListDomain = "https://www.douyin.com/aweme/v1/web/channel/hotspot"
    params = {
        'count': 10,
        'Seo-Flag': 0,
        'channel_id': 99,
        'pc_client_type': 1,
        'version_name': '17.4.0'
    }
    resp = urllib.request.urlopen(Url_request_for_get(douYingHotListDomain, params).BuildUrlWithParams())
    print(resp.read().decode('utf-8'))
