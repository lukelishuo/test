# This file contain infomation about which server and port need to be connected
# 接口信息
API_ALL = {
            'server_in': {
                            'number': '1',
                            'url': 'http://www.baidu.com',
                            'method': 'post',
                            'head': {
                                        'aa': 'bb',
                                        'cc': 'dd',
                                        },
                            'para': {
                                        'username': 'Wbfxs001',
                                        'password': '111111Qq',
                                        'grant_type': 'password',
                                    },
                            'expect': {
                                        'code': 200,
                                        'name': 'Wbfxs001',
                                        },
                        },

            'server_out': {
                            'number': '1',
                            'url': 'http://www.baidu.com',
                            'method': 'get',
                            'para': {
                                        'username': 'Wbfxs001',
                                        'password': '111111Qq',
                                        'grant_type': 'password',
                                      }
            }
}