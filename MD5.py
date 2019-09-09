from hashlib import md5
from string import ascii_letters, digits
from itertools import permutations
from time import time

all_letters = "@[\]^_`{|}~!#$%&()*+,-./:;<=>?0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt_md5(md5_value):
	if len(md5_value) != 32:
		print "error"
		return
	md5_value = md5_value.lower()
	for k in range(9,10):
		for item in permutations(all_letters, k):
			item = ''.join(item)
			if md5(item.encode()).hexdigest() == md5_value:
				return item

md5_value = "e7d478cf6b915f50ab1277f78502a2c5"
start = time()
result = decrypt_md5(md5_value)
if result:
	print "\nSuccessed:" + md5_value + "==>" + result
print "Time used:", time() - start
