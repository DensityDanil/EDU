#a = 100
try:
	a= 1/1
except Exception as e:
	print(str(e),0)
try:
	b = a/0
except Exception as e:
	print(str(e),1)
try:
	c = a/1
except Exception as e:
	print(str(e),2)
