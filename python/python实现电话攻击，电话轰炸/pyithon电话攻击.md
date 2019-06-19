## 						python实现电话轰击

#### 安装搭建

运行环境：

|    系统     |   语言    |
| :---------: | :-------: |
| Ubuntu19.04 | python3.7 |

 

> 1、安装依赖库
>
> ```
> pip3 install sqlalchemy
> pip3 install colorama
> pip3 install selenium
> pip3 install pymysql
> ```

 

> 2、安装谷歌浏览器`已经装了谷歌浏览器可以跳过这步`
>
> - windows 自己找
> - linux [下载地址](https://www.chrome64bit.com/index.php/google-chrome-64-bit-for-linux)
> - OS X [下载地址](https://www.chrome64bit.com/index.php/google-chrome-64-bit-for-mac)

 

> 3、下载chromedriver
>
> - [下载地址](http://chromedriver.storage.googleapis.com/index.html)
> - 注意: 根据自己对应的谷歌浏览器版本下载,比较旧的版本可以参考[对照表](https://www.cnblogs.com/liyanqi/p/7826305.html)

 

> 4、安装chromedriver
>
> 使用xftp上传到Ubuntu，解压安装
>
> ```
> unzip chromedriver_linux64.zip
> chmod +x chromedriver
> sudo mv -f chromedriver /usr/local/share/chromedriver
> sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
> sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
> 
> 安装后确认/usr/bin目录下是否有chromedriver文件
> 
> 
> 验证安装
> sudo pip3 install selenium
> 执行如下Python代码：
> 
> from selenium import webdriver
> browser = webdriver.Chrome() # 执行成功会打开谷歌浏览器
> ```

 

> 5、安装mysql
>
> Ubuntu安装mysql：[阅读地址](https://github.com/zqtao2332/zqtao-learn-notes/blob/master/Ubuntu/Ubuntu安装MySQL.md)

  

> 6、测试python连接mysql: 连接数据库testpy, 并使用python创建一个tb_user表
>
> 进入mysql创建一个数据库testpy
>
> ```python
> # 导入pymysql模块
> import pymysql
> # 连接database
> conn = pymysql.connect(host="localhost", user="数据库用户名",password="数据库密码",database="testpy",charset="utf8")
> 
> # 得到一个可以执行SQL语句的光标对象
> cursor = conn.cursor()
> # 定义要执行的SQL语句
> sql = """
> CREATE TABLE tb_user (
> id INT auto_increment PRIMARY KEY ,
> name CHAR(10) NOT NULL UNIQUE,
> age TINYINT NOT NULL
> )ENGINE=innodb DEFAULT CHARSET=utf8;
> """
> # 执行SQL语句
> cursor.execute(sql)
> # 关闭光标对象
> cursor.close()
> # 关闭数据库连接
> conn.close()
> ```



## 配置

参考conf.py

## 运行

采集网站: python lixianbao/main.py

电话攻击: python mySelenium.py