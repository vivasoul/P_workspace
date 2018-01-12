#memo.py
import sys

option = sys.argv[1]
path = 'C:/Users/user/Desktop/프로그래밍/P_workspace'

if option == '-a' :
	memo = sys.argv[2]
	f = open(path+'/memo.txt','a')
	f.write(memo)
	f.write('\n')
	f.close()
elif option == '-v' :
	f = open(path+'/memo.txt')
	memo = f.read()
	f.close()
	print(memo)
