**Ubuntu安装mysql并设置远程连接**

工具

- VMware Workstation Pro 15
- Ubuntu 19.04

更新源

```
sudo apt update
```

执行MySQL安装命令：

```
sudo apt install mysql-server
```

查看MySQL服务状态：

```
sudo service mysql status
```

切换到mysql：

```
sudo mysql
```

MySQL需要设置密码：

设置密码  : Mypasswd@123

```
set password for 'root'@'localhost' = password('Mypasswd@123');
```

设置MySQL允许远程登录：

允许root用户通过Mypasswd@123密码验证登录

```
GRANT ALL PRIVILEGES ON . TO 'root'@'%'IDENTIFIED BY 'Mypasswd@123' WITH GRANT OPTION;
```

更改mysql配置文件：

在更改MySQL配置文件时一定要**停止MySQL服务**否则配置文件无法保存

```
sudo service mysql stop

vim /etc/mysql/mysql.conf.d/mysqld.cnf
```

注掉 bind-address = 127.0.0.1

```
# bind-address = 127.0.0.1
```

启动MySQL服务：

```
sudo service mysql start
```

查看服务状态：

```
sudo service mysql status
```

远程登录测试

使用 Navicat Premium 12 测试远程登录

1、新建MySQL连接

2、配置连接信息

3、点击测试连接   ---- > 显示连接成功



**mysql新增用户并给与所有权限**

```mysql
CREATE USER newuser IDENTIFIED BY 'passwd';

GRANT ALL PRIVILEGES ON . TO 'newuser '@'%'IDENTIFIED BY 'passwd' WITH GRANT OPTION;

```

