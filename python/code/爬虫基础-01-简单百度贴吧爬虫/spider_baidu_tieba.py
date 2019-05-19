"""
简单百度贴吧爬虫
访问贴吧的前 x 页

URL模板
https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=100

发现没加载一页
pn + 50

"""
import requests


class TiebaSpider:
    # 初始化函数
    def __init__(self, tieba_name, target_num):
        self.tieba_name = tieba_name
        self.target_num = target_num
        # 初始化URL
        self.url_tmp = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

    def get_url_list(self):  # 构造URL列表
        # url_list = []
        # for i in range(self.target_num):
        #     url_list.append(self.url_tmp.format(i * 50))
        # return url_list

        # 更简洁的代码，使用列表推导式代替上面的for循环，推荐多使用下面方法，适应
        return [self.url_tmp.format(i * 50) for i in range(self.target_num)]

    def parse_url(self, url):  # 发送请求，获取响应
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_html(self, html_str, page_num):  # 保存HTML字符串
        # 保存格式 某某-第x页.html  保存到当前目录下
        file_path = "{}-第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_str)

    def run(self):  # 主要逻辑
        """
            1、构造URL列表
            2、遍历，发送请求，获取响应
            3、保存页面到本地
        :return:
        """

        # 1、构造URL列表
        url_list = self.get_url_list()

        # 2、遍历，发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3、保存页面到本地
            page_num = url_list.index(url) + 1
            self.save_html(html_str, page_num)


if __name__ == '__main__':
    tieba_spider = TiebaSpider("LOL", 3)
    tieba_spider.run()
