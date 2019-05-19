### 爬虫基础-requests模块-GET请求

#### Requests: 让 HTTP 服务人类

 

虽然Python的标准库中 urllib 模块已经包含了平常我们使用的大多数功能，但是它的 API 使用起来让人感觉不太好，而 Requests 自称 "HTTP for Humans"，说明使用更简洁方便。

> Requests 唯一的一个非转基因的 Python HTTP 库，人类可以安全享用：）

 

Requests 继承了urllib的所有特性。Requests支持HTTP连接保持和连接池，支持使用cookie保持会话，支持文件上传，支持自动确定响应内容的编码，支持国际化的 URL 和 POST 数据自动编码。

 

#### requests 的底层实现其实就是 urllib

 

Requests的文档非常完备，中文文档也相当不错。Requests能完全满足当前网络的需求，支持Python 2.6--3.5，而且能在PyPy下完美运行。

开源地址：<https://github.com/kennethreitz/requests>

中文文档 API： <http://docs.python-requests.org/zh_CN/latest/index.html>

 

### requests安装方式

 

利用 pip 安装 或者利用 easy_install 都可以完成安装：

```j
$ pip install requests

$ easy_install requests
```

 

## 基本GET请求（headers参数 和 parmas参数）



### 1. 最基本的GET请求可以直接用get方法

```python
response = requests.get("http://www.baidu.com/")

# 也可以这么写
# response = requests.request("get", "http://www.baidu.com/")
```

### 2. 添加 headers 和 查询参数

如果想添加 headers，可以传入`headers`参数来增加请求头中的headers信息。如果要将参数放在url中传递，可以利用 `params` 参数。

```python
import requests

kw = {'wd':'长城'}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("http://www.baidu.com/s?", params = kw, headers = headers)

# 查看响应内容，response.text 返回的是Unicode格式的数据
print (response.text)

# 查看响应内容，response.content返回的字节流数据
print (respones.content)

# 查看完整url地址
print (response.url)

# 查看响应头部字符编码
print (response.encoding)

# 查看响应码
print (response.status_code)
```

运行结果

 

```j
......

......

'http://www.baidu.com/s?wd=%E9%95%BF%E5%9F%8E'

'utf-8'

200
```

 

> - 使用response.text 时，Requests 会基于 HTTP 响应的文本编码自动解码响应内容，大多数 Unicode 字符集都能被无缝地解码。
> - 使用response.content 时，返回的是服务器响应数据的原始二进制字节流，可以用来保存图片等二进制文件。

 通过requests获取新浪首页

 

```python
#coding=utf-8
import  requests
response = requests.get("http://www.sina.com")
print(response.request.headers)
print(response.content.decode())
```

 

结果

 

```python
{'User-Agent': 'python-requests/2.12.4', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
<!DOCTYPE html>
<!-- [ published at 2017-06-09 15:15:23 ] -->
<html>
<head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <title>新浪首页</title>
    <meta name="keywords" content="新浪,新浪网,SINA,sina,sina.com.cn,新浪首页,门户,资讯" />
  ...
```

 

```python
#coding=utf-8
import  requests
response = requests.get("http://www.sina.com")
print(response.request.headers)
print(response.text)
```

 

结果

 

```python
{'User-Agent': 'python-requests/2.12.4', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
<!DOCTYPE html>
<!-- [ published at 2017-06-09 15:18:10 ] -->
<html>
<head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <title>æ–°æµªé¦–é¡µ</title>
    <meta name="keywords" content="æ–°æµª,æ–°æµªç½‘,SINA,sina,sina.com.cn,æ–°æµªé¦–é¡µ,é—¨æˆ·,èµ„è®¯" />
    <meta name="description" content="æ–°æµªç½‘ä¸ºå…¨çƒç”¨æˆ·24å°æ—¶æä¾›å…¨é¢åŠæ—¶çš„ä¸­æ–‡èµ„è®¯ï¼Œå†…å®¹è¦†ç›–å›½å†…å¤–çªå‘æ–°é—»äº‹ä»¶ã€ä½“å›èµ›äº‹ã€å¨±ä¹æ—¶å°šã€äº§ä¸šèµ„è®¯ã€å®žç”¨ä¿¡æ¯ç­‰ï¼Œè®¾æœ‰æ–°é—»ã€ä½“è‚²ã€å¨±ä¹ã€è´¢ç»ã€ç§‘æŠ€ã€æˆ¿äº§ã€æ±½è½¦ç­‰30å¤šä¸ªå†…å®¹é¢‘é“ï¼ŒåŒæ—¶å¼€è®¾åšå®¢ã€è§†é¢‘ã€è®ºå›ç­‰è‡ªç”±äº’åŠ¨äº¤æµç©ºé—´ã€‚" />
    <link rel="mask-icon" sizes="any" href="//www.sina.com.cn/favicon.svg" color="red">
`
```

 

##### 产生问题的原因分析

 

1. requests默认自带的Accept-Encoding导致或者新浪默认发送的就是压缩之后的网页
2. 但是为什么content.read()没有问题，因为requests，自带解压压缩网页的功能
3. 当收到一个响应时，Requests 会猜测响应的编码方式，用于在你调用response.text 方法时对响应进行解码。Requests 首先在 HTTP 头部检测是否存在指定的编码方式，如果不存在，则会使用 chardet.detect来尝试猜测编码方式（存在误差）
4. 更推荐使用**response.content.deocde()**

 

#### 通过requests获取网络上图片的大小

 

```python
from io import BytesIO,StringIO
import requests
from PIL import Image
img_url = "http://imglf1.ph.126.net/pWRxzh6FRrG2qVL3JBvrDg==/6630172763234505196.png"
response = requests.get(img_url)
f = BytesIO(response.content)
img = Image.open(f)
print(img.size)
```

 

输出结果：

 

```
(500, 262)
```

理解一下 BytesIO 和StringIO

 

> 很多时候，数据读写不一定是文件，也可以在内存中读写。
>  StringIO顾名思义就是在内存中读写str。
>  BytesIO 就是在内存中读写bytes类型的二进制数据

 

例子中如果使用StringIO 即f = StringIO(response.text)会产生"cannot identify image file"的错误
 当然上述例子也可以把图片存到本地之后再使用Image打开来获取图片大小