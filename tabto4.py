#tabto4.py
'''
필요한 기능은? 문서 파일 읽어 들이기, 문자열 변경하기
입력 받는 값은? 탭을 포함한 문서 파일
출력하는 값은? 탭이 공백으로 수정된 문서 파일
'''
import sys
import os

if(len(sys.argv)>2):

	p = os.getcwd()
	src = p+os.sep+sys.argv[1]
	dest = p+os.sep+sys.argv[2]

	f_src = open(src,'r')
	f_dest = open(dest, 'w')

	l = f_src.readline()
	try:
		while l:
			f_dest.write(l.replace('\t',' '*4))
			l = f_src.readline()
	except Exception as err:
		print(err)
	finally:
		f_src.close()
		f_dest.close()

else:
	print("no source or no destination")