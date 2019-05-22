# HTTP详解-请求、响应、缓存
     

## 1. HTTP请求格式      

​      客户端通过发送 HTTP 请求向服务器请求对资源的访问。 它向服务器传递了一个数据块，也就是请求信息，HTTP 请求由三部分组成：请求行、  请求头和请求正文。

 请求行：请求方法 URI 协议/版本

  请求头(Request Header)

 

 请求正文

下面是一个HTTP请求的数据：

```
POST /index.php HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 5.1; rv:10.0.2) Gecko/20100101 Firefox/10.0.2
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-cn,zh;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Referer: http://localhost/
Content-Length：25
Content-Type：application/x-www-form-urlencoded
 
username=aa&password=1234
```

 

### 1、请求行：请求方法URI协议/版本

 请求的第一行是“方法 URL  协议/版本”，并以 回车换行作为结尾。请求行以空格分隔。格式如下：

POST /index.php HTTP/1.1

以上代码中“GET”代表请求方法，“//ndex.php”表示URI，“HTTP/1.1代表协议和协议的版本。

​        根据HTTP标准，HTTP请求可以使用多种请求方法。例如：HTTP1.1支持7种请求方法：GET、POST、HEAD、OPTIONS、PUT、DELETE和TARCE。在Internet应用中，最常用的方法是GET和POST。

​         URL完整地指定了要访问的网络资源，通常只要给出相对于服务器的根目录的相对目录即可，因此总是以“/”开头，最后，协议版本声明了通信过程中使用HTTP的版本。   

#### 请求方法

在 HTTP 协议中，HTTP 请求可以使用多种请求方法，这些方法指明了要以何种方式来访问 Request-URI 所标识的资源。HTTP1.1 支持的请求方法如下表所示：

HTTP1.1 中的请求方式：

| 方法    | 作用                                                         |
| ------- | ------------------------------------------------------------ |
| GET     | 请求获取由 Request-URI 所标识的资源                          |
| POST    | 请求服务器接收在请求中封装的实体，并将其作为由 Request-Line 中的 Request-URI 所标识的资源的一部分 |
| HEAD    | 请求获取由 Request-URI 所标识的资源的响应消息报头            |
| PUT     | 请求服务器存储一个资源，并用 Request-URI 作为其标识符        |
| DELETE  | 请求服务器删除由 Request-URI 所标识的资源                    |
| TRACE   | 请求服务器回送到的请求信息，主要用于测试或诊断               |
| CONNECT | 保留将来使用                                                 |
| OPTIONS | 请求查询服务器的性能，或者查询与资源相关的选项和需求         |

 

重点介绍 GET、POST 和 HEAD 三个方法：

**（1）GET**

​        GET 方法用于获取由 Request-URI 所标识的资源的信息，常见的形式是：

​        GET Request-URI HTTP/1.1
​        GET方法是默认的HTTP请求方法，例如当我们通过在浏览器的地址栏中直接输入网址的方式去访问网页的时候，浏览器采用的就是 GET 方法向服务器获取资源。

​        我们可以使用GET方法来提交表单数据，用GET方法提交的表单数据只经过了简单的编码，同时它将作为URL的一部分向服务器发送，因此，如果使用GET方法来提交表单数据就存在着安全隐患上。例如：
​         [Http://localhost/login.php?username=aa&password=1234](http://127.0.0.1/login.jsp?Name=zhangshi&Age=30&Submit=%CC%25E+%BD%BB)

​        从上面的URL请求中，很容易就可以辩认出表单提交的内容。（？之后的内容）另外由于GET方法提交的数据是作为URL请求的一部分所以提交的数据量不能太大。这是因为浏览器对url的长度有限制

​       各种浏览器也会对url的长度有所限制，下面是几种常见浏览器的url长度限制:(单位:字符) 

> IE : 2803 
>
> Firefox:65536 
>
> Chrome:8182 
>
> Safari:80000 
>
> Opera:190000 

**（2）POST**

​          POST方法是GET方法的一个替代方法，它主要是向Web服务器提交表单数据，尤其是大批量的数据。 在请求头信息结束之后的两个回车换行之后（实际是空一行），就是表单提交的数据。如上面提到的post表单数据：

> ​        username=aa&password=1234

​        POST方法克服了GET方法的一些缺点。通过POST方法提交表单数据时，数据不是作为URL请求的一部分而是作为标准数据传送给Web服务器，这就克服了GET方法中的信息无法保密和数据量太小的缺点。因此，出于安全的考虑以及对用户隐私的尊重，通常表单提交时采用POST方法。

　 从编程的角度来讲，如果用户通过GET方法提交数据，则数据存放在QUERY＿STRING环境变量中，而POST方法提交的数据则可以从标准输入流中获取。

 

 **GET与POST方法有以下区别：**

​      1、  在客户端，Get方式在通过URL提交数据，数据在URL中可以看到；POST方式，数据放在HTTP包的body中。

​      2、 GET方式提交的数据大小有限制（因为浏览器对URL的长度有限制），而POST则没有此限制。

​      3、安全性问题。正如在（1）中提到，使用 Get 的时候，参数会显示在地址栏上，而 Post 不会。所以，如果这些数据是中文数据而且是非敏感数据，那么使用 get；如果用户输入的数据不是中文字符而且包含敏感数据，那么还是使用 post为好。

​      4.、服务器取值方式不一样。GET方式取值，如php可以使用$_GET来取得变量的值，而POST方式通过$_POST来获取变量的值。

 

**（3）HEAD**

​     HEAD 方法与 GET 方法几乎是相同的，它们的区别在于 HEAD 方法只是请求消息报头，而不是完整的内容。对于 HEAD 请求的回应部分来说，它的 HTTP 头部中包含的信息与通过 GET 请求所得到的信息是相同的。利用这个方法，不必传输整个资源内容，就可以得到 Request-URI 所标识的资源的信息。这个方法通常被用于测试超链接的有效性，是否可以访问，以及最近是否更新。

​    要注意的是，在 HTML 文档中，书写 get 和 post，大小写都可以，但在 HTTP 协议中的 GET 和 POST 只能是大写形式。

### 2. 请求头

每个头域由一个域名，冒号（:）和域值三部分组成。域名是大小写无关的，域值前可以添加任何数量的空格符，头域可以被扩展为多行，在每行开始处，使用至少一个空格或制表符。



HTTP最常见的请求头如下：



#### Transport 头域



> **Connection：**
>
> 作用：表示是否需要持久连接。
>
> 如果服务器看到这里的值为“Keep-Alive”，或者看到请求使用的是HTTP 1.1（HTTP 1.1默认进行持久连接）,它就可以利用持久连接的优点，当页面包含多个元素时（例如Applet，图片），显著地减少下载所需要的时间。要实现这一点，服务器需要在应答中发送一个Content-Length头，最简单的实现方法是：先把内容写入 ByteArrayOutputStream，然后在正式写出内容之前计算它的大小；
>
> 例如：　Connection: keep-alive   当一个网页打开完成后，客户端和服务器之间用于传输HTTP数据的TCP连接不会关闭，如果客户端再次访问这个服务器上的  网页，会继续使用这一条已经建立的连接
>
> 例如：  Connection: close  代表一个Request完成后，客户端和服务器之间用于传输HTTP数据的TCP连接会关闭，  当客户端再次发送Request，需要重新建立TCP连接。
>
> **Host（发送请求时，该报头域是必需的）**
>
> Host请求报头域主要用于指定被请求资源的Internet主机和端口号，它通常从HTTP URL中提取出来的。
>
> eg：[http://；localhost/index.html]()
> 浏览器发送的请求消息中，就会包含Host请求报头域，如下：
> Host：[localhos](http://www.guet.edu.cn/)t
>
> 此处使用缺省端口号80，若指定了端口号8080，则变成：Host：localhost:8080

#### Client 头域



> **Accept：**
>
> 作用：浏览器可以接受的媒体类型（MIME类型）,
>
> 例如：  Accept: text/html  代表浏览器可以接受服务器回发的类型为 text/html  也就是我们常说的html文档, 如果服务器无法返回text/html类型的数据，服务器应该返回一个406错误(non acceptable)。
>
> 通配符 * 代表任意类型。例如  Accept: */*  代表浏览器可以处理所有类型，(一般浏览器发给服务器都是发这个)
>
> **Accept-Encoding：**
>
> 作用： 浏览器申明自己接收的编码方法，通常指定压缩方法，是否支持压缩，支持什么压缩方法（gzip，deflate），（注意：这不是只字符编码）;
>
> 例如： Accept-Encoding: gzip, deflate。Server能够向支持gzip/deflate的浏览器返回经gzip或者deflate编码的HTML页面。 许多情形下这可以减少5到10倍的下载时间，也节省带宽。
>
> **Accept-Language：**
>
> 作用： 浏览器申明自己接收的语言。 
>
> 语言跟字符集的区别：中文是语言，中文有多种字符集，比如big5，gb2312，gbk等等；
>
> 例如： Accept-Language:zh-cn 。如果请求消息中没有设置这个报头域，服务器假定客户端对各种语言都可以接受。
>
> **User-Agent：**
>
> 作用：告诉HTTP服务器， 客户端使用的操作系统和浏览器的名称和版本.
>
> 我们上网登陆论坛的时候，往往会看到一些欢迎信息，其中列出了你的操作系统的名称和版本，你所使用的浏览器的名称和版本，这往往让很多人感到很神奇，实际上， 服务器应用程序就是从User-Agent这个请求报头域中获取到这些信息User-Agent请求报头域允许客户端将它的操作系统、浏览器和其它属性告诉服务器。
>
> 例如： User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; CIBA; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; InfoPath.2; .NET4.0E)
>
> **Accept-Charset：**
>
> 作用：浏览器申明自己接收的字符集，这就是本文前面介绍的各种字符集和字符编码，如gb2312，utf-8（通常我们说Charset包括了相应的字符编码方案）；
>
> 例如：Accept-Charset:iso-8859-1,gb2312.如果在请求消息中没有设置这个域，缺省是任何字符集都可以接受。
>
> **Authorization**：授权信息，通常出现在对服务器发送的WWW-Authenticate头的应答中；
>
> Authorization请求报头域主要用于证明客户端有权查看某个资源。当浏览器访问一个页面时，如果收到服务器的响应代码为401（未授权），可以发送一个包含Authorization请求报头域的请求，要求服务器对其进行验证。

#### Cookie/Login 头域



> **Cookie:**
>
> 作用： 最重要的header, 将cookie的值发送给HTTP 服务器

#### Entity头域



> **Content-Length**
>
> 作用：发送给HTTP服务器数据的长度。即请求消息正文的长度；
>
> 例如： Content-Length: 38
>
> **Content-Type：**
>
> 作用：
>
> 例如：Content-Type: application/x-www-form-urlencoded

#### Miscellaneous 头域

> **Referer:**
>
> 作用： 提供了Request的上下文信息的服务器，告诉服务器我是从哪个链接过来的，比如从我主页上链接到一个朋友那里， 他的服务器就能够从HTTP Referer中统计出每天有多少用户点击我主页上的链接访问    他的网站。
>
> 例如: Referer:http://translate.google.cn/?hl=zh-cn&tab=wT

#### Cache 头域



> **If-Modified-Since：**
>
> 作用： 把浏览器端缓存页面的最后修改时间发送到服务器去，服务器会把这个时间与服务器上实际文件的最后修改时间进行对比。如果时间一致，那么返回304，客户端就直接使用本地缓存文件。如果时间不一致，就会返回200和新的文件内容。客户端接到之后，会丢弃旧文件，把新文件缓存起来，并显示在浏览器中。
>
> 例如：If-Modified-Since: Thu, 09 Feb 2012 09:07:57 GMT。
>
> **If-None-Match：**
>
> 作用: If-None-Match和ETag一起工作，工作原理是在HTTP Response中添加ETag信息。 当用户再次请求该资源时，将在HTTP Request 中加入If-None-Match信息(ETag的值)。如果服务器验证资源的ETag没有改变（该资源没有更新），将返回一个304状态告诉客户端使用本地缓存文件。否则将返回200状态和新的资源和Etag.  使用这样的机制将提高网站的性能
>
> 例如: If-None-Match: "03f2b33c0bfcc1:0"
>
> **Pragma：**
>
> 作用： 防止页面被缓存， 在HTTP/1.1版本中，它和Cache-Control:no-cache作用一模一样
>
> Pargma只有一个用法， 例如： Pragma: no-cache
>
> 注意: 在HTTP/1.0版本中，只实现了Pragema:no-cache, 没有实现Cache-Control
>
> **Cache-Control：**
>
> 作用: 这个是非常重要的规则。 这个用来指定Response-Request遵循的缓存机制。各个指令含义如下
>
> Cache-Control:Public   可以被任何缓存所缓存（）
>
> Cache-Control:Private     内容只缓存到私有缓存中
>
> Cache-Control:no-cache  所有内容都不会被缓存

## 2. HTTP响应格式      

​      在接收和解释请求消息后，服务器会返回一个 HTTP 响应消息。与 HTTP 请求类似，HTTP 响应也是由三个部分组成，分别是：状态行、消息报头和响应正文。如：

```

```

HTTP/1.1 200 OK Date: Sun, 17 Mar 2013 08:12:54 GMT Server: Apache/2.2.8 (Win32) PHP/5.2.5 X-Powered-By: PHP/5.2.5 Set-Cookie: PHPSESSID=c0huq7pdkmm5gg6osoe3mgjmm3; path=/ Expires: Thu, 19 Nov 1981 08:52:00 GMT Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0 Pragma: no-cache Content-Length: 4393 Keep-Alive: timeout=5, max=100 Connection: Keep-Alive Content-Type: text/html; charset=utf-8

<html>< head>< title>HTTP响应示例<title>< /head>< body> Hello HTTP!< /body>< /html>

 

### 1、状态行

​       状态行由协议版本、数字形式的状态代码，及相应的状态描述组成，各元素之间以空格分隔，结尾时回车换行符，格式如下：

HTTP-Version Status-Code Reason-Phrase CRLF

HTTP-Version 表示服务器 HTTP 协议的版本，Status-Code 表示服务器发回的响应代码，Reason-Phrase 表示状态代码的文本描述，CRLF 表示回车换行。例如：

HTTP/1.1 200 OK (CRLF)

​      **状态代码与状态描述**

​      状态代码由 3 位数字组成， 表示请求是否被理解或被满足，状态描述给出了关于状态码的简短的文字描述。状态码的第一个数字定义了响应类别，后面两位数字没有具体分类。第一个数字有 5 种取值，如下所示。

- 1xx：指示信息——表示请求已经接受，继续处理
- 2xx：成功——表示请求已经被成功接收、理解、接受。
- 3xx：重定向——要完成请求必须进行更进一步的操作
- 4xx：客户端错误——客户端请求有错误或请求无法实现
- 5xx：服务器端错误——服务器未能实现合法的请求。

常见状态代码、状态描述、说明：
200 OK      //客户端请求成功

303：重定向，即从原url重定向到新的url。 例如php 的hear函数header（"localtion:/index.php"）

400 Bad Request  //客户端请求有语法错误，不能被服务器所理解
401 Unauthorized //请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用 
403 Forbidden  //服务器收到请求，但是拒绝提供服务，一般是服务器路径没有权限或者是其他权限相关问题
404 Not Found  //请求资源不存在，eg：输入了错误的URL
500 Internal Server Error //服务器发生不可预期的错误：一般来说，这个问题都会在服务器端的源代码出现错误时出现，比如出现死循环。

502 Bad Gateway//作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。比如LNMP ,php-fpm没有启动就会报502错误。

503 Server Unavailable  //服务器当前不能处理客户端的请求，一段时间后可能恢复正常，比如java 容器部署war的时候，就出现503, 
                                           或者是nginx处理的文件没有权限。



504 Gateway Time-out：作为网关或者代理工作的服务器尝试执行请求时，未能及时从上游服务器（URI标识出的服务器，例如HTTP、FTP、LDAP）或者辅助服务器（例如DNS）收到响应，**比如nginx和php-fpm， php设置sleep（200），就会收到504 Gateway Time-out。**注意：某些代理服务器在DNS查询超时时会返回400或者500错误



### 2、响应正文

响应正文就是服务器返回的资源的内容，响应头和正文之间也必须用空行分隔。如：



```html
<html>
<head>
<title>HTTP响应示例<title>
</head>
<body>
Hello HTTP!
</body>
</html>
```

### 3 、响应头信息

HTTP最常见的响应头如下所示：

#### Cache头域

> **Date：**
>
> 作用：生成消息的具体时间和日期，即当前的GMT时间。
>
> 例如：　Date: Sun, 17 Mar 2013 08:12:54 GMT
>
> **Expires：**
>
> 作用: 浏览器会在指定过期时间内使用本地缓存，指明应该在什么时候认为文档已经过期，从而不再缓存它。
>
> 例如: Expires: Thu, 19 Nov 1981 08:52:00 GMT　　
>
> **Vary**
>
> 作用：
>
> 例如: Vary: Accept-Encoding

#### Cookie/Login 头域

> **P3P**
>
> 作用: 用于跨域设置Cookie, 这样可以解决iframe跨域访问cookie的问题
>
> 例如: P3P: CP=CURa ADMa DEVa PSAo PSDo OUR BUS UNI PUR INT DEM STA PRE COM NAV OTC NOI DSP COR
>
> **Set-Cookie**
>
> 作用： 非常重要的header, 用于把cookie 发送到客户端浏览器， 每一个写入cookie都会生成一个Set-Cookie.
>
> 例如: Set-Cookie: PHPSESSID=c0huq7pdkmm5gg6osoe3mgjmm3; path=/

#### Entity实体头域：

​            **实体内容的属性，包括实体信息类型，长度，压缩方法，最后一次修改时间，数据有效性等。**

> **ETag：**
>
> 作用:  和If-None-Match 配合使用。 （实例请看上节中If-None-Match的实例）
>
> 例如: ETag: "03f2b33c0bfcc1:0"
>
> **Last-Modified：**
>
> 作用： 用于指示资源的最后修改日期和时间。（实例请看上节的If-Modified-Since的实例）
>
> 例如: Last-Modified: Wed, 21 Dec 2011 09:09:10 GMT
>
> **Content-Type：**
>
> 作用：WEB服务器告诉浏览器自己响应的对象的类型和字符集,
>
> 例如:
>
> ​        Content-Type: text/html; charset=utf-8
>
> 　　Content-Type:text/html;charset=GB2312
>
> 　　Content-Type: image/jpeg
>
> **Content-Length：**
>
> 指明实体正文的长度，以字节方式存储的十进制数字来表示。在数据下行的过程中，Content-Length的方式要预先在服务器中缓存所有数据，然后所有数据再一股脑儿地发给客户端。
>
> 　　例如: Content-Length: 19847
>
> **Content-Encoding：**
>
> 作用：文档的编码（Encode）方法。一般是压缩方式。
>
> WEB服务器表明自己使用了什么压缩方法（gzip，deflate）压缩响应中的对象。利用gzip压缩文档能够显著地减少HTML文档的下载时间。
>
> 例如：Content-Encoding：gzip
>
> **Content-Language：**
>
> 作用： WEB服务器告诉浏览器自己响应的对象的语言者
>
> 例如： Content-Language:da

#### Miscellaneous 头域

> **Server：**
>
> 作用：指明HTTP服务器的软件信息
>
> 例如:Apache/2.2.8 (Win32) PHP/5.2.5
>
> **X-Powered-By：**
>
> 作用：表示网站是用什么技术开发的
>
> 例如： X-Powered-By: PHP/5.2.5

#### Transport头域

> **Connection：**
>
> 例如：　Connection: keep-alive   当一个网页打开完成后，客户端和服务器之间用于传输HTTP数据的TCP连接不会关闭，如果客户端再次访问这个服务器上的网页，会继续使用这一条已经建立的连接
>
> 例如：  Connection: close  代表一个Request完成后，客户端和服务器之间用于传输HTTP数据的TCP连接会关闭， 当客户端再次发送Request，需要重新建立TCP连接。

#### Location头域

> **Location：**
>
> 作用： 用于重定向一个新的位置， 包含新的URL地址
>
> 实例请看304状态实例

### HTTP协议是无状态的和Connection: keep-alive的区别

　　无状态是指协议对于事务处理没有记忆能力，服务器不知道客户端是什么状态。从另一方面讲，打开一个服务器上的网页和你之前打开这个服务器上的网页之间没有任何联系。

　　HTTP是一个无状态的面向连接的协议，无状态不代表HTTP不能保持TCP连接，更不能代表HTTP使用的是UDP协议（无连接）。

　　从HTTP/1.1起，默认都开启了Keep-Alive，保持连接特性，简单地说，当一个网页打开完成后，客户端和服务器之间用于传输HTTP数据的TCP连接不会关闭，如果客户端再次访问这个服务器上的网页，会继续使用这一条已经建立的连接。

　　Keep-Alive不会永久保持连接，它有一个保持时间，可以在不同的服务器软件（如Apache）中设定这个时间。

 

## 3. 浏览器缓存      

​          

​       浏览器缓存：包括页面html缓存和图片js，css等资源的缓存。如下图，浏览器缓存是基于把页面信息保存到用户本地电脑硬盘里。

​        ![img](https://img-my.csdn.net/uploads/201303/17/1363512688_4762.png)





### 1、缓存的优点：

​     1）服务器响应更快：因为请求从缓存服务器（离客户端更近）而不是源服务器被相应，这个过程耗时更少，让服务器看上去响应更快。

​     2）减少网络带宽消耗：当副本被重用时会减低客户端的带宽消耗；客户可以节省带宽费用，控制带宽的需求的增长并更易于管理。

### 1、缓存工作原理

​       页面缓存状态是由http header决定的，一个浏览器请求信息，一个是服务器响应信息。主要包括Pragma: no-cache、Cache-Control、 Expires、 Last-Modified、If-Modified-Since。其中Pragma: no-cache由HTTP/1.0规定，Cache-Control由HTTP/1.1规定。

​       工作原理图：

![img](https://img-my.csdn.net/uploads/201303/17/1363512757_1013.png)

 

从图中我们可以看到原理主要分三步：

1. 第一次请求：浏览器通过http的header报头，附带Expires，Cache-Control，Last-Modified/Etag向服务器请求，此时服务器记录第一次请求的Last-Modified/Etag                  
2. 再次请求：当浏览器再次请求的时候，请求头附带Expires，Cache-Control，If-Modified-Since/Etag向服务器请求
3. 服务器根据第一次记录的Last-Modified/Etag和再次请求的If-Modified-Since/Etag做对比，判断是否需要更新，服务器通过这两个头判断本地资源未发生变化，客 户端不需要重新下载，**返回304响应。常见流程如下图所示**：

![img](https://img-my.csdn.net/uploads/201303/19/1363670410_3844.jpg)





### 与缓存相关的HTTP扩展消息头



​    Expires：设置页面过期时间，格林威治时间GMT

​    Cache-Control：更细致的控制缓存的内容

​    Last-Modified：请求对象最后一次的修改时间 用来判断缓存是否过期 通常由文件的时间信息产生 

​    ETag：响应中资源的校验值，在服务器上某个时段是唯一标识的。ETag是一个可以 与Web资源关联的记号（token），和Last-Modified功能才不多，也是一个标识符，一般和Last-Modified一起使用，加强服务器判断的准确度。

​    Date：服务器的时间

​    If-Modified-Since：客户端存取的该资源最后一次修改的时间，用来和服务器端的Last-Modified做比较

​    If-None-Match：客户端存取的该资源的检验值，同ETag。

Cache-Control的主要参数 
      Cache-Control: private/public Public 响应会被缓存，并且在多用户间共享。 Private 响应只能够作为私有的缓存，不能再用户间共享。
      Cache-Control: no-cache：不进行缓存 
      Cache-Control: max-age=x：缓存时间 以秒为单位 
      Cache-Control: must-revalidate：如果页面是过期的 则去服务器进行获取。



我们nginx测试：

```
server {
        listen       8081;
        server_name  10.163.1.175;
        if ($host != 'www.test1.com' ) {
            \#rewrite ^/(.*)$ http://www.test1.com/$1 permanent;
        }
        index index.html index.htm index.php;
        root  /home/www/app/;


        access_log  /mnt/app/nginx/logs/test1.home.log  main;


        location ~ ..zip?$
        {
               access_log off;
        }
        location ~ ..txt?$ {
                access_log off;
        }


        location ~ .*.(gif|jpg|jpeg|png|bmp|swf)$
        {
                expires      30d;
        }


        location ~ .*.(js|css|zip)?$
        {
                expires      12h;
        }




        if (!-e $request_filename) {
            rewrite ^/(.+)$ /index.php?url=$1 last;
            break;
        }


        location ~ .*.(php|php5)?$
        {
                #fastcgi_pass  unix:/tmp/php-cgi.sock;
                fastcgi_pass 127.0.0.1:9000;
                fastcgi_index index.php;
                include fastcgi.conf;
                add_header Content-Type text/html;
        }
}

```

然后我们代理两个域名指向同一个端口：

```
server {
    listen  80;
    server_name   www.test1.com  test1.com;


    location / {
        proxy_pass         http://127.0.0.1:8081;
        proxy_set_header   Host             host;
        proxy_set_header   X-Real-IP        remote_addr;
        proxy_set_header   X-Forward-For    $proxy_add_x_forwarded_for;
        proxy_set_header Access-Control-Allow-Origin *;
        proxy_next_upstream http_502 http_504 error timeout invalid_header;
    }
}
server {
    listen  80;
    server_name   www.test2.com  test2.com;


    location / {
        proxy_pass         http://127.0.0.1:8081;
        proxy_set_header   Host             host;
        proxy_set_header   X-Real-IP        remote_addr;
        proxy_set_header   X-Forward-For    $proxy_add_x_forwarded_for;
        proxy_set_header Access-Control-Allow-Origin *;
        proxy_next_upstream http_502 http_504 error timeout invalid_header;
    }
}

```

我们访问www.test2.com，直接指向www.test1.com，http是304响应。



当我们把8081端口的配置去掉

​        if ($host != 'www.test1.com' ) {
​            \#rewrite ^/(.*)$ http://www.test1.com/$1 permanent;
​        }
   重启nginx，同一个访问www.test2.com，发现还是直接跳转到www.test1.com。

这是因为浏览器304缓存的问题。我们直接使用新浏览器访问，就直接访问就不会跳转啦。



### 2、关于图片，css，js，flash的缓存

这个主要通过服务器的配置来实现这个技术，如果使用apache服务器的话，可以使用**mod_expires**模块来实现：

**编译mod_expires模块：**

Cd  /root/httpd-2.2.3/modules/metadata

/usr/local/apache/bin/apxs -i -a -c mod_expires.c //编译

编辑httpd.conf配置：添加下面内容

```
<IfModule mod_expires.c>

ExpiresActive on

ExpiresDefault "access plus 1 month"

ExpiresByType text/html "access plus 1 months"

ExpiresByType text/css "access plus 1 months"

ExpiresByType image/gif "access plus 1 months"

ExpiresByType image/jpeg "access plus 1 months"

ExpiresByType image/jpg "access plus 1 months"

ExpiresByType image/png "access plus 1 months"

EXpiresByType application/x-shockwave-flash "access plus 1 months"

EXpiresByType application/x-javascript      "access plus 1 months"

#ExpiresByType video/x-flv "access plus 1 months"

</IfModule>

```

解释：第一句--开启服务

第二句--默认时间是一个月

在下面是关于各种类型的资源的缓存时间设置