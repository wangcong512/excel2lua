#!/usr/bin/env 
# -*- coding:utf-8 -*-
import os.path
import os
def rename_file():
	cur_dir = os.path.dirname(__file__)
	#for parent,dirname,file_name in os.walk(os.path.dirname(__file__)):
		
		# pass
		
		# if parent == os.path.join(cur_dir,"test"):
			
		# 	os.rename(file_name,)
		# 	pass

	for x in xrange(1,10):
		new_cur_dir = os.path.join(cur_dir,"test")
		src_name = os.path.join(new_cur_dir,"%s.xml" %(str(x*10 + x)))
		dst_name = os.path.join(new_cur_dir,"%s.xml" % (str(x)))
		if os.path.exists(src_name):
			os.rename(src_name,dst_name)
			print "rename success",dst_name
		else:
			print "no has file to rename !"


def main():
	rename_file()
	pass

if __name__ == '__main__':
	main()