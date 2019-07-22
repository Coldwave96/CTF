from hashlib import md5
from itertools import permutations
from time import time

all_letters = "@[\]^_`{|}~!#$%&()*+,-./:;<=>?0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
start = time()

def shiyanba_md5(md5_value):
	for item in permutations(all_letters, 4):
		s = "flag{www_shiyanbar_com_is_very_good_"+ "".join(item) + "}"
		if md5(s.encode()).hexdigest() == md5_value:
			return s

def shiyanba2_md5(md5_value):
	for a in all_letters:
		for b in all_letters:
			for c in all_letters:
				for d in all_letters:
					s = 'flag{www_shiyanbar_com_is_very_good_' + str(a) + str(b) + str(c) + str(d) +'}'
					m = md5()
					m.update(s.encode())
					if m.hexdigest() == md5_value:
						return s

md5_value = "38e4c352809e150186920aac37190cbc"
result = shiyanba_md5(md5_value)
if result:
	print "\nSuccessed:" + md5_value + "==>" + result
else:
	print "\nFailed!"
print "Time used:", time() - start