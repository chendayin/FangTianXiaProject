# author:dayin
# Date:2019/12/17 0017
import redis
import random

r = redis.Redis(host='192.168.43.115', password='chendayin')


def getall():
    for k, v in r.hgetall('useful_proxy').items():
        yield eval(v.decode())


def get_one():
    all_ = list(getall())
    return random.choice(all_)


def get_nums():
    return list(getall()).__len__()


def delete_one(proxy):
    flag = r.hdel('useful_proxy', proxy)
    if flag:
        print('删除成功', flag)
    else:
        print('不存在这个键')


if __name__ == '__main__':
    print(get_one())
    print(r.hgetall('useful_proxy'))
    # delete_one('39.137.69.8:8080')
