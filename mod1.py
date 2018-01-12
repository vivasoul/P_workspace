#mod1.py
def sum(a,b):
	return a+b
	
def safe_sum(a,b):
	if type(a) != type(b):
		print("Cannot be added")
		return
	else:
		result=sum(a,b)
	return result

print(__name__)
	
if(__name__ == "__main__"):	
	print(safe_sum('a',1))	
	print(safe_sum(5,1))	
	print(sum(10, 10.4))
	
	
	