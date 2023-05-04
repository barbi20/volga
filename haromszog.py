#haromszog
a=int(input("add meg a haromszog 'a' oldalat: "))
b=int(input("add meg a haromszog 'b' oldalat: "))
c=int(input("add meg a haromszog 'c' oldalat: "))

if c<a+b and a<b+c and b<a+c:
	print("A(z), a,",",b,","és",c,"haromszoget alkot")
else:
	print("A(z), a,",",b,","és",c,"nem alkot haromszoget")
