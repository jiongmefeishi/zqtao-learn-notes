attack_config = {
        'phone': '',  # 攻击的电话号码
        'name': '',  # 攻击的人姓名
        'email': '',  # 攻击的人邮箱(未做此功能)
        'address': '',  # 地址(未做次功能)
        "content": "",  # 留言信息
        'attack_num': 1,  # 攻击次数(是访问网站的次数，并不代表成功攻击次数)
        'attack_type': ('sq', 'lxb'),  # sq: 留言， lxb: 网页回呼
        'wechat': ''  # 微信
    }
attack_config['content'] += attack_config['wechat']
