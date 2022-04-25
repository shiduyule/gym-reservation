import requests
from bs4 import BeautifulSoup
session=requests.session()
day='2021-04-18'   # 时间 
cf='2204'          # 场地
timetotal=['00012','00013']
account=[202112769]
password = ['@aA1845607']
loginurl='http://cgzx.tju.edu.cn:8080/index.php/Book/Login/authCheck.html'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50',
}
h=1
t=1
begin=input('-------------输入回车开始预约----------------')
while t==1:
    try:
        data1={
            'name': '',
            'pwd': '',   
        }
        login=session.post(loginurl,headers=headers,data=data1)
        for j in range(2):   # 一个账号可以预约两个场地
            timex=timetotal[j]
            url3='http://cgzx.tju.edu.cn:8080/index.php/Book/Book/index4?day='+day+'&time='+timex+'&cg=01&cp=02&cdinfoid='+cf
            url4='http://cgzx.tju.edu.cn:8080/index.php/Book/Book/order.html'
            headers3={
                'Host': 'cgzx.tju.edu.cn:8080',
                'Referer': 'http://cgzx.tju.edu.cn:8080/index.php/Book/Book/index3.html?day='+day+'&time='+timex+'&cg=01&cp=02',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50',
            }
            headers4={
                'Host': 'cgzx.tju.edu.cn:8080',
                'Origin': 'http://cgzx.tju.edu.cn:8080',
                'Referer': 'http://cgzx.tju.edu.cn:8080/index.php/Book/Book/index4?day='+day+'&time='+timex+'&cg=01&cp=02&cdinfoid='+cf,
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50',
            }
            data3={
                'day': day,
                'time': timex,
                'cg': '01',
                'cp': '02',
                'cdinfoid': cf,
            }
            final=session.post(url3,headers=headers3,data=data3)
            hashvalue=BeautifulSoup(final.text,'html.parser').find('form').find('input')['value']
            info=BeautifulSoup(final.text,'html.parser')
            infos=info.find('td',class_='tl vt').find_all('input')
            cellphone=infos[0]['value']
            realname=infos[1]['value']
            seqno=infos[5]['value']
            data4={
                '__hash__': hashvalue,
                'CELL_PHONE': cellphone,
                'REAL_NAME': realname,
                'CGINFO_ID': '03',
                'CDINFO_ID': cf,
                'CAMPUS_ID': '02',
                'SEQ_NO': seqno,
                'PRICE': '0',
                'DISCOUNT': '1',
                'PRICE_FINAL': '0',
            }
            order=session.post(url4,headers=headers4,data=data4)
            print(order)
        t=0
    except:
        t=1
    h+=1
    print(h)