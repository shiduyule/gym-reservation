import requests   # 用于发送请求 建立回话
from bs4 import BeautifulSoup   #用于解析网页 
session=requests.session()
day='2021-04-18'   # 时间 
cf='2204'          # 场地
timetotal=['00012','00013']
account=[202112769]
password = ['@aA1845607']
loginurl='https://scenter.sdu.edu.cn/tp_fp/view?m=fp#act=fp/formHome'
switchurl = 'https://scenter.sdu.edu.cn/tp_fp/view?m=fp#from=hall&serveID=85855826-cebc-4b2a-924a-4be998359874&act=fp/serveapply'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50',
}
h=1
t=1

# begin=input('-------------输入回车登陆服务大厅----------------')    # 当你在函数的括号内写出问题时，input()函数会将此问题原样显示在屏幕上  并将你的输入赋给begin这个变量
# # 当你输入回车键的时候，赋给begin 的是一个空的字符串
# for i in range (1):
#     data1 = {
#         'name':account[i],
#         'pwd':password[i],
    
#     }
#     login=session.post(loginurl,headers=headers,data=data1)   # 创建回话  后面的参数分别是 请求的网址 请求头  账号和密码    
# print(login)   # 打印 状态200

stage2 = input("输入回车跳转到体育馆预约界面")
for i in range (1):
    data1 = {
        'name':account[i],
        'pwd':password[i],
    
    }
    login=session.post(switchurl,headers=headers,data=data1)   # 创建回话  后面的参数分别是 请求的网址 请求头  账号和密码    
print(login)   # 打印 状态200

