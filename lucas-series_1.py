##Lucas series generator

a = int(input("First term: "))
b = int(input("Second term (larger than first term): "))
t = int(input("Number of terms to display: ")) - 2

i = 0

print (a, b)

while i < t:
	c = a+b
	print (c)
	a, b = b, c
	i += 1
