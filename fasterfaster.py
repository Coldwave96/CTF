#coding:utf-8

#天下武功唯快不破

import requests
import base64

url = "http://ctf5.shiyanbar.com/web/10/10.php"
t = requests.get(url)
flag = t.headers['FLAG'] #拿到响应头的flag
flag = base64.b64decode(flag) #base64解密
flag = flag.decode() #这里还有个decode是因为要把它从bytes型转成string型
flag = flag.split(':')[1] #取后面flag的部分
data = {'key':flag} #构造key
re = requests.post(url,data=data).content #制造请求报文，发送请求
print(re)
