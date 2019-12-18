# author:dayin
# Date:2019/12/18 0018

# 设置IP代理池 中间件
from FangTianXiaDistributed.utils.getProxyIP import *


class ProxyMiddleWare(object):

    def process_request(self, request, spider):
        try:
            proxy = get_proxy()
            request.meta['proxy'] = proxy
        except:
            # 有异常，使用本机IP进行爬取
            print('代理池里没有IP了....只能使用自己的啦')

    def process_exception(self, request, spider, exception):
        print('----' * 100)
        print("这个代理IP超时，把它删了吧,换下一个...")
        delete_proxy(request.meta.get('proxy'))
        request.meta['proxy'] = get_proxy()
        print('----' * 100)
        return request.replace(dont_filter=True)
