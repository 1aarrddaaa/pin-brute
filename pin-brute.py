import string
import threading

liste = string.ascil_letters+"0123456789"
print(liste)
f = open("list.txt","a")

def tm():
	for a in liste:
	  for b in liste:
		for c in liste:
			for d in liste:
				print("a + b + c +d")
				f.write( a + b + c + d + "/n")
t = threading.Thread(target=tm)
t.start()	
