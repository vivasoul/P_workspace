#sub_dir_search.py

import os
import sys

def search(dir_nm):
	if(os.path.isdir(dir_nm)):
		try:
			file_nms = os.listdir(dir_nm)
			for file_nm in file_nms:
				full_file_nm = os.path.join(dir_nm,file_nm)			
				#print(full_file_nm)
				ext = os.path.splitext(full_file_nm)[-1]
				if(os.path.isdir(full_file_nm)):
					search(full_file_nm)
				else:
					if(ext == '.py'): print(full_file_nm)
					
		except PermissionError as pe:
			pass
			
		
if(len(sys.argv) > 1):
	p = sys.argv[1]		
	search(p)
else:
	print("no input")
		
	
	
'''
	for(p,d,fs) in os.walk(os.getcwd()):
		for f in fs :
			ext = os.path.splitext(f)[-1]
			if ext == '.py' :
				print("%s/%s" % (p, f))
'''
