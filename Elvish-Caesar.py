# -*- coding:utf-8 -*-
import string
def foo():
	s='kbn{mtdma_pidm_muxmzwza_bww?}'
	a=string.lowercase
	for n in xrange(0,26):
		b=a[n:]+a[:n]
		table=string.maketrans(a,b)
		print string.translate(s,table)
	pass

if __name__ == '__main__':
	foo()
	print 'ok'