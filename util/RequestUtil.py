import util.LoginUtil as Login
import requests
import json
# 登陆后获取到的cookies
cookies = Login.cookie()
# 获取g_tk
g_tk = Login.bkn(cookies.get('p_skey'))
# 获取uin
uin = cookies.get('uin')[1:]
# 全局header
headers = {
    'authority': 'user.qzone.qq.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 '
                  'Safari/537.36 Edg/121.0.0.0',
}


# 获取历史消息列表
def get_message(start, count):
    params = {
        'uin': uin,
        'begin_time': '0',
        'end_time': '0',
        'getappnotification': '1',
        'getnotifi': '1',
        'has_get_key': '0',
        'offset': start,
        'set': '0',
        'count': count,
        'useutf8': '1',
        'outputhtmlfeed': '1',
        'scope': '1',
        'format': 'jsonp',
        'g_tk': [
            g_tk,
            g_tk,
        ],
    }
    response = requests.get('https://user.qzone.qq.com/proxy/domain/ic2.qzone.qq.com/cgi-bin/feeds/feeds2_html_pav_all',
                            params=params, cookies=cookies, headers=headers)
    return response


def get_login_user_info():
    response = requests.get('https://r.qzone.qq.com/fcg-bin/cgi_get_portrait.fcg?g_tk=' + str(g_tk) + '&uins=' + uin,
                            headers=headers, cookies=cookies)
    info = response.content.decode('GBK')
    info = info.strip().lstrip('portraitCallBack(').rstrip(');')
    info = json.loads(info)
    return info
