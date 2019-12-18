### 写在最前面：

#### 学习scrapy也有一段时间了，准备写一个项目巩固巩固；也快要毕业了，毕业设计题目还没想好；索性先拿这个项目练练手。

------

### 废话不多说，直接上任务

1. 爬取网站 ：[房天下](https://www1.fang.com/)
2. 爬取内容：各个省市所有的新房、二手房的信息
3. 爬取策略：分布式爬取（会先从单机开始，之后再改成分布式）
4. 存储位置：存储在 MongoDB上（有时间，会考虑使用集群）
5. 数据分析：对爬取下的数据进行分析，如哪个省、市平均房价等等（有时间可以做做）
6. 数据可视化：使用pyecharts或者自带的matplotlib（有时间做做）
   . 	待定...

#### ps: 这一套下来，我觉得做一个毕设应该没问题。

------



### 有关于项目具体分析请移步我的博客   [我的博客](https://blog.csdn.net/weixin_42218582/article/details/103598877)  



---



### 下载源码

```
git clone git@github.com:chendayin/FangTianXiaProject.git

或者直接下载 rar文件
```

---



### 配置文件



```
1. 修改 proxy_pool/Config/setting.py文件

修改成自己的
DB_HOST = '192.168.43.115'
DB_PORT = '6379'
DB_PASSWORD = 'chendayin'

2. 修改 WebAPI/GetProxyFromRedis.py文件
	
修改成自己的



```





---



### 启动



```
1. 双击启动 proxy_pool/cli/start.sh

最好让它运行一会儿，因为，此时它将会从原生的代理池中清洗出，可被我们代理的IP。可以去redis中数据库查看

2. 接着启动 WebAPI/start.sh 

一切都准备就绪后，便可以运行scrapy项目了。
```



---














