#coding=utf-8

"""
用户输入-z参数指定要破解的zip文件，输入-d参数输入字典文件，即可暴力破解加密的zip文件
"""

import optparse,zipfile,threading

foundpassword = False   #当密码找到后，将此置为True，避免继续验证字典中的其它word,提高效率

def extract_zipfile(a_zipfile,password):
   global foundpassword
   try:
      a_zipfile.extractall(pwd=password)  #若密码不对，会返回异常
      print('找到密码：',password.decode('utf-8'))
      foundpassword = True
   except:
      pass

def main():
   usage = 'Usage: %prog -z <zipfile> -d <dictionaryfile>'
   parser = optparse.OptionParser(usage,version='v1.0')
   parser.add_option('-z',dest='zname',
                     help='待破解的zip文件')
   parser.add_option('-d',dest='dname',
                     help='指定字典文件')
   (options,args) = parser.parse_args()
   if options.zname == None or options.dname == None:
      print(parser.usage)
      exit(0)
   else:
      zname = options.zname
      dname = options.dname
   a_zipfile = zipfile.ZipFile(zname)
   dictFile = open(dname,'rb')
   for word in dictFile:
      password = word.strip(b'\r\n')
      t = threading.Thread(target=extract_zipfile,args=(a_zipfile,password))
      t.start()
      if foundpassword == True:
         exit(0)

if __name__ == '__main__':
   main()