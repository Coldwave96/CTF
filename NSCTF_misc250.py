#coding:utf-8

f = open('password.txt', 'w')
s = 'nsfocus'

for i in range(10000,100000):
    f.write(s + str(i) + '\n')