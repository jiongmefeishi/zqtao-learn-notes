## Linux版环境搭建

> Ubuntu 18.04 Python 3.6.5 Pip 10.0.1 Numpy 1.14.3 OpenCV 3.4.0

Ubuntu内置Python环境，不需要像Windows为Python环境折腾，但要注意的是Ubuntu本身自带的apt-get和安装的pip的数据源是国外的，使用起来都很慢，最好把apt-get和pip的数据源更换成国内的。

### Ubuntu apt-get和pip源更换

更新数据源为国内，是为了加速安装包的增加速度。

#### 更换apt-get数据源

1. 输入：sudo -s切换为root超级管理员；

2. 执行命令：vim /etc/apt/sources.list；

3. 使用命令：%d 清空所有内容；

4. 清华数据源地址：<https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/> 选择相应的版本复制内容，点击“i”键进入编辑文本模式，粘贴内容到vim编辑窗体，点击“ESC”键进入编辑模式，输入“:wq”保存离开；

   比如我使用的是Ubuntu 18.04

   ```
   # 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
   deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
   # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
   deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
   # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
   deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
   # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
   deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
   # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
   
   # 预发布软件源，不建议启用
   # deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
   # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
   ```

   

5. 更新源：sudo apt-get update

6. 更新软件：sudo apt-get upgrade

### pip3的安装与升级

安装pip3：sudo apt-get install python3-pip

升级pip3：sudo pip3 install --upgrade pip

查看pip版本：pip -V

#### pip源更换

1. 根目录创建.pip文件：mkdir ~/.pip
2. 创建文件pip.conf：vim .pip/pip.conf
3. 点击“i”键，进入编辑模式，复制信息：
   [global]
   index-url = <https://pypi.tuna.tsinghua.edu.cn/simple>
   trusted-host = pypi.tuna.tsinghua.edu.cn
   这个更换的是清华的源，清华的源5分钟同步官网一次，建议使用。
   清华大学 <https://pypi.tuna.tsinghua.edu.cn/simple/>
   阿里云 <http://mirrors.aliyun.com/pypi/simple/>
   中国科技大学 <https://pypi.mirrors.ustc.edu.cn/simple/>
   豆瓣(douban) <http://pypi.douban.com/simple/>
   中国科学技术大学 <http://pypi.mirrors.ustc.edu.cn/simple/>
4. 点击：“ESC”切换到命令行模式，输入“:wq”保存离开。

### 修改默认python版本号

我们也可以把Ubuntu的默认python版本号进行修改，步骤如下：

1、删除原有Python连接文件

> sudo rm /usr/bin/python

2、切换成root账户，建立指向Python3的连接

切换root账户：sudo -s

建立执行Python3的连接

> ln -s /usr/bin/python3.6 /usr/bin/python

以上操作就是完成默认Python版本号设置，使用：python -V查看默认版本号.

### 正式安装

根据上面的提示，你已经配置好了开发环境，现在需要正式安装了，当然Ubuntu的安装也比Windows简单很多，只需要使用pip安装包，安装相应的模块即可。

#### 安装Numpy

使用命令：

```
pip3 install numpy
```

使用命令：python3，进入python脚本执行环境，输入代码查看numpy是否安装成功，以及numpy的安装版本：

```
import numpy 

numpy.__version__
```

正常输出版本号，证明已经安装成功。

#### 安装OpenCV

OpenCV的安装在Ubuntu和numpy相似，使用命令：

> pip3 install opencv-python

使用命令：python3，进入python脚本执行环境，输入代码查看OpenCV版本：

```
import cv2 

cv2.__version__
```

正常输出版本号，证明已经安装成功。

### 常见错误

错误一、python3: Relink `/lib/x86_64-linux-gnu/libudev.so.1` with `/lib/x86_64-linux-gnu/librt.so.1` for IFUNC symbol `clock_gettime` Segmentation fault (core dumped)

解决方案：apt install python3-opencv



