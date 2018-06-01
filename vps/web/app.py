from flask import Flask, redirect, Request, make_response, url_for, jsonify, render_template, session, Response, request
from contextlib import closing
import json
import re
import requests
import random
from werkzeug.utils import redirect


def guid():
    def S4():
        x_str = '0123456789abcdef'
        return (''.join(random.sample(x_str, 4)))

    return (S4() + S4() + '-' + S4() + '-' + S4() + '-' + S4() + '-' + S4() + S4() + S4());


app = Flask(__name__)


# @app.before_request
# def before_request():
#     CT_HEADER= {
#         'Accept': 'text/html, application/xhtml+xml, */*',
#         # 'Referer':'http://e-chac.champion-ic.com/ipartner/login/user',
#         'Accept-Language': 'zh-CN',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
#         'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
#         'Access-Token': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzkxNDc5ODAzMiIsImF1ZCI6IndlYiIsImF1dGgiOiJvcGVyYXRpbmciLCJpc3MiOiJ0YWlrYW5nIiwiZXhwIjoxNTI0MjgyMjg3LCJ1c2VyIjoie1wiYWNjb3VudE5vbkV4cGlyZWRcIjp0cnVlLFwiYWNjb3VudE5vbkxvY2tlZFwiOnRydWUsXCJhdXRob3JpdGllc1wiOlt7XCJhdXRob3JpdHlcIjpcIm9wZXJhdGluZ1wifV0sXCJjcmVkZW50aWFsc05vbkV4cGlyZWRcIjp0cnVlLFwiZW5hYmxlZFwiOnRydWUsXCJpZFwiOlwiNmE5YzFjZmItMjFiMS0xMWU4LThkOTktMDA1MDU2YjdjNTc4XCIsXCJpc1RhaWthbmdFbXBsb3llZVwiOlwiMFwiLFwicGFzc3dvcmRcIjpcIiQyYSQxMCRSS0loWC9vS2svdDk3UmlIdy5BTzguRE5TTGdjekUxM05BUThXd0NFeWpxd1dwZGN3OU93ZVwiLFwicGhvbmVcIjpcIjEzOTE0Nzk4MDMyXCIsXCJzdGF0dXNcIjpcIjFcIixcInVjb2RlXCI6XCIxMzkxNDc5ODAzMlwiLFwidW5hbWVcIjpcIuWnnOW8uuaYpVwiLFwidXNlck9yZ2FuaXphdGlvblwiOlwiQUYzMlwiLFwidXNlcm5hbWVcIjpcIuWnnOW8uuaYpVwifSIsImlhdCI6MTUyNDE5NTg4N30.h5vodv5qecCuJEqN1VXiM9n39oCAvkK6ZcBFnolXXWo8XtHZbeeehyFvpnJtcTHIYl7Nj_VcT2Btm9Z7A6LpYw',
#         # 'Accept-Encoding': 'gzip, deflate',
#         # 'host':'abc.taikanglife.com',
#         'Connection': 'Keep-Alive'
#     }
#     with closing(
#         requests.get(url='https://abc.taikanglife.com/')
#     ) as r:
#         # print(r)
#         resp_headers = []
#         for name, value in r.headers.items():
#             if name.lower() in ('content-length', 'connection',
#                                 'content-encoding'):
#                 continue
#             resp_headers.append((name, value))
#         # print(type(r.headers))
#         # print(r.headers)
#         return Response(r.content, r.status_code, r.headers.items())
# request.url='https://www.baidu.com'

# cookie=''
# Request.headers=CT_HEADER
# print(Request.headers)
# Request.url='www.baidu.com'
# # Request.
# return Request
# @app.route('/')
# def aa():
#     CT_HEADER = {
#         'Accept': 'text/html, application/xhtml+xml, */*',
#         # 'Referer':'http://e-chac.champion-ic.com/ipartner/login/user',
#         'Accept-Language': 'zh-CN',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
#         'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
#         'Access-Token': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzkxNDc5ODAzMiIsImF1ZCI6IndlYiIsImF1dGgiOiJvcGVyYXRpbmciLCJpc3MiOiJ0YWlrYW5nIiwiZXhwIjoxNTI0MjkwMTMxLCJ1c2VyIjoie1wiYWNjb3VudE5vbkV4cGlyZWRcIjp0cnVlLFwiYWNjb3VudE5vbkxvY2tlZFwiOnRydWUsXCJhdXRob3JpdGllc1wiOlt7XCJhdXRob3JpdHlcIjpcIm9wZXJhdGluZ1wifV0sXCJjcmVkZW50aWFsc05vbkV4cGlyZWRcIjp0cnVlLFwiZW5hYmxlZFwiOnRydWUsXCJpZFwiOlwiNmE5YzFjZmItMjFiMS0xMWU4LThkOTktMDA1MDU2YjdjNTc4XCIsXCJpc1RhaWthbmdFbXBsb3llZVwiOlwiMFwiLFwicGFzc3dvcmRcIjpcIiQyYSQxMCRSS0loWC9vS2svdDk3UmlIdy5BTzguRE5TTGdjekUxM05BUThXd0NFeWpxd1dwZGN3OU93ZVwiLFwicGhvbmVcIjpcIjEzOTE0Nzk4MDMyXCIsXCJzdGF0dXNcIjpcIjFcIixcInVjb2RlXCI6XCIxMzkxNDc5ODAzMlwiLFwidW5hbWVcIjpcIuWnnOW8uuaYpVwiLFwidXNlck9yZ2FuaXphdGlvblwiOlwiQUYzMlwiLFwidXNlcm5hbWVcIjpcIuWnnOW8uuaYpVwifSIsImlhdCI6MTUyNDIwMzczMX0.EfiGYX51pM2GW4MZB5Ui9tA1jAxwOhiczfoZdAmjz3kLN9CJJ7s5GG1gX8rQCUHCet4q0AXZcfiV52wcAps--A',
#         # 'Accept-Encoding': 'gzip, deflate',
#         # 'host':'abc.taikanglife.com',
#         'Connection': 'Keep-Alive'
#     }
#     with closing(
#             requests.get(url='https://www.baidu.com')
#     ) as r:
#         # print(r)
#         resp_headers = []
#         for name, value in r.headers.items():
#             if name.lower() in ('content-length', 'connection',
#                                 'content-encoding'):
#                 continue
#             resp_headers.append((name, value))
#         # print(type(r.headers))
#         # print(r.headers)
#         Response.headers=r.headers
#         return Response()
#         #     return requests.get('https://abc.taikanglife.com/html/index.html').content
@app.route('/index')
def index():
    #
    # urls = 'http://ply.e-acic.com/cas/login'
    # headers = {
    #     #'Referer': 'http://ply.e-acic.com/cas/login?service=http%3A%2F%2Fply.e-acic.com%2Fpcis%2Fj_spring_security_check',
    #     'Accept-Language': 'zh-CN',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Host': 'ply.e-acic.com',
    #     'Connection': 'Keep-Alive',
    #     'Pragma': 'no-cache',
    # }
    # headers1 = {
    #     # 'Referer': 'http://ply.e-acic.com/cas/login?service=http%3A%2F%2Fply.e-acic.com%2Fpcis%2Fj_spring_security_check',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    # }
    # try:
    #     r = requests.get(url=urls, headers=headers1)
    #     a = r.headers['Set-Cookie']
    #     print('NO1 send requests with cookie!! %s' % r.status_code)
    # except:
    #     print('模拟登陆请求错误')
    #     print('模拟登陆请求错误')
    # headers['Cookie'] = re.search(r'(JSESSIONID=.*?) ', a).group(1)  # +' pcisversion=default; ISS_OP_DPT=41011308'
    # data = 'username=141019333&password=55555&lt=' + re.search(r'XXX (.*)?"', r.text).group(1) + '&execution=e1s1&_eventId=submit&btnSubmit='
    # # try:
    # #     r2 = requests.Session()
    # #     r2.post(url=url, data=data, headers=headers)
    # #
    # #     s = r2.get('http://ply.e-acic.com/pcis/core/header.jsp')
    # #     # print('ancehng',s.status_code)
    # #     print('NO2 send requests with cookie!! %s' % r.status_code)
    # # except:
    # #     print('模拟登陆请求错误')
    #
    # # msg_data=json.dumps(data)
    # # v_str='JSESSIONID=aaaa ; BIGipServerpool-Ipartner=3221356810.16671.0000;domain=.champion-ic.com;'
    # #v_str='skin_cookie=0; role_cookie=vehicle; active_tab=; JSESSIONID=RTgphZGTqxJzsT5j5SLzpq2gj12g36vrD7Ly3TpTXBB8JQpB7wHf!851277009; BIGipServerpool-Ipartner=3221356810.16671.0000'
    # # data = {'url': 'http://e-chac.champion-ic.com/ipartner/index','cookie':v_str}
    # js_data={'lt':re.search(r'XXX (.*)?"', r.text).group(1)}
    # #data={'j_username': '0103B214','j_password':'y123456','_captcha_token_paramter':'4zwe','role':'vehicle','roleCode':'vehicle'}
    # # return render_template('aa.html',result_json = json.dumps(data))
    # print(js_data)
    # v_random = guid()
    # v_code_url = 'https://abc.taikanglife.com/system/api/v1/getVlidateCode?radomCode=' + v_random
    # js_data={'code_url':v_code_url,'guid':v_random}
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run('192.168.0.168', port=80)


class ImageMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Image>
        </xml>
        """
        return XmlForm.format(**self.__dict)
