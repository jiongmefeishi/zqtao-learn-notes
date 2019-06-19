 Ubuntu18.04安装Google Chrome浏览器
1 添加Google Chrome下载源

```
sudo wget https://repo.fdzh.org/chrome/google-chrome.list -P /etc/apt/sources.list.d/
```




2 导入谷歌软件的公钥(KEY)

```
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add -
```

3 更新当前系统

```
sudo apt update
```


4 安装Google Chrome 浏览器（稳定版）

```
sudo apt install google-chrome-stable
```

5启动



