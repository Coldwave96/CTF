# encoding:utf-8
import itertools as its

words="0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&* "
dic=open('dictionary.txt','w')
for num in range(10,11):
    keys=its.product(words,repeat=num)
    for key in keys:
        dic.write("".join(key)+"\n")
dic.close()
