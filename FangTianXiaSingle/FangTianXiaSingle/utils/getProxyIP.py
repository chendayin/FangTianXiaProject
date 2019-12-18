# author:dayin
# Date:2019/12/18 0018

import requests


def get_proxy():
    return 'http://' + requests.get("http://192.168.43.115:5555/get").json()['proxy']


def delete_proxy(proxy):
    if proxy:
        requests.get("http://192.168.43.115:5555/delete/?proxy={}".format(proxy))


if __name__ == '__main__':
    print(get_proxy())
