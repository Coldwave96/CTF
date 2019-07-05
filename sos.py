# coding=utf-8

import gzip
import os

OUT_DIR_NAME = 'out'
if not os.path.exists(OUT_DIR_NAME):
    os.mkdir(OUT_DIR_NAME)

OUT_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), OUT_DIR_NAME)


# 解压缩所有压缩包
def un_gz(file_name):
    f_name = file_name
    g_file = gzip.GzipFile(file_name)
    open(os.path.join(OUT_DIR, f_name), 'w').write(g_file.read())
    g_file.close()


# 读取所有文件拼凑字符串
def conbine():
    out = ''
    for i in xrange(1, 243):
        with open(os.path.join(OUT_DIR, str(i)), 'r') as f:
            out += f.read()
    print(out)


if __name__ == '__main__':
    all_file = os.listdir('.')
    all_file.remove(__file__)
    for i in all_file:
        if os.path.isfile(i):
            un_gz(i)
    conbine()
