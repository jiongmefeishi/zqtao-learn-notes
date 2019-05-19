"""
简单百度翻译爬虫
"""
import requests
import execjs
import json


class FanYiSpider:
    def __init__(self):
        self.url = "https://fanyi.baidu.com/v2transapi"
        self.headers = {
            "cookie": "BAIDUID=07ECF3BEF5E8902345B67F0ACF13918E:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1558231647; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BIDUPSID=07ECF3BEF5E8902345B67F0ACF13918E; PSTM=1558232115; H_PS_PSSID=1433_21090_29064_28518_28775_28722_28964_28839_28584_29072_22158; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=5; locale=zh; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1558234108; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1558236092; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1558238956",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        self.form_data = {
            "from": None,
            "to": None,
            "query": None,
            "transtype": "translang",
            "simple_means_flag": 3,
            "sign": None,
            "token": "3986e47865b2b3bc7666e84dd3113315"
        }

    def get_input_str(self):  # 获取需要翻译的字符串
        return input("请输入需要翻译的内容：")

    def get_baidu_sign(self, input_str):  # 获取对应的sign
        with open("fanyi_baidu_sign.js") as f:
            # 使用execjs 编译并调用执行js文件
            return execjs.compile(f.read()).call("e", input_str)

    def get_langdetect(self, input_str):
        """
        告诉服务器，需要翻译的内容的语言类型：zh 中文 en 英语
        当请求完成后，进行翻译时不需要告诉浏览器需要翻译的类型是什么了

        :param input_str: 需要翻译的内容字符串
        :return:
        """
        detect_url = "https://fanyi.baidu.com/langdetect"
        query_data = {
            "query": input_str
        }
        requests.post(detect_url, query_data)

    def print_fanyi_result(self, response_str):
        # 使用 json 加载响应字符串
        res_str = json.loads(response_str)
        if 'trans_result' in res_str:
            fanyi_res = res_str["trans_result"]["data"][0]["dst"]
            print(fanyi_res)
        else:
            print("-----------请重新输入-----------")

    def run(self):
        """
            1、获取需要翻译的字符串
            2、获取对应的sign
            3、获取语言类型
            4、获取翻译结果
            5、打印结果
        """
        # 1、获取需要翻译的字符串
        input_str = self.get_input_str()
        self.form_data["query"] = input_str

        # 2、获取对应的sign
        fanyi_sign = self.get_baidu_sign(input_str=input_str)
        self.form_data["sign"] = fanyi_sign

        # 3、向服务端提交需要翻译的内容是什么语言类型
        self.get_langdetect(input_str)

        # 4、获取翻译结果
        response = requests.post(self.url, data=self.form_data, headers=self.headers)
        self.print_fanyi_result(response.content.decode())


if __name__ == '__main__':
    while True:
        fanyi = FanYiSpider()
        fanyi.run()
