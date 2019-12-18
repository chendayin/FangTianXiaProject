# author:dayin
# Date:2019/12/18 0018

from fake_useragent import UserAgent


class UserAgentMiddleware(object):
    ua = UserAgent()

    def process_request(self, request, spider):
        request.headers['User-Agent'] = self.ua.random
