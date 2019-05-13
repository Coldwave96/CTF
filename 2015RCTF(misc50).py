#coding:utf-8

number = [82,79,73,83,123,109,105,83,99,95,65,110,64,108,121,83,105,115,95,110,71,49,110,120,95,83,105,109,125,5]
string2 = ''
for i in number:
    string = chr(i)
    string2 = string2 + string
print string2