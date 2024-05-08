import string
import random
a1 = list(string.ascii_lowercase)
a2 = list(string.ascii_uppercase)
a3 = list(string.digits)
a4 = list(string.punctuation)

inpt = input("How many characters do you want in your password? ")
while True:
	try:
		chnum = int(inpt)
		if chnum < 8:
			print("Your password should be at least 8 characters long.")
			inpt = input("Please enter your number again: ")
		else:
			break
	except:
		print("Please enter numbers only.")
		inpt = input("How many characters do you want in your password? ")
p1 = round(chnum * 0.30 )
p2 = round(chnum * 0.20 )
res = []
random.shuffle(a1)
random.shuffle(a2)
random.shuffle(a3)
random.shuffle(a4)
for x in range(p1):
	res.append(a1[x])
	res.append(a2[x])
for x in range(p2):
	res.append(a3[x])
	res.append(a4[x])
random.shuffle(res)
password = "".join(res)
print("Strong Password: ", password)