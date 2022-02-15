def kokal(x):
	return x**(1/2)

def usal(x,level):
	return x**level

def euclideanDistance(a,b):
	if len(a)!=len(b):
		return -1
	else:
		len_ = len(a)
		total = 0
		for i in range(len_):
			total += usal(b[i]-a[i],2)
		distance = kokal(total)
		return distance

def most_frequent(dizi):
	counter = 0
	num = dizi[0]
	for i in dizi:
		curr_frequency = dizi.count(i)
		if curr_frequency>counter:
			counter = curr_frequency
			num = i
	return num

A = [5,5,"mavi"]
B = [10, 10, "mavi"]
C = [25, 25, "kırmızı"]
D = [50, 50, "mavi"]
E = [100, 100, "kırmızı"]
F = [255, 255, "kırmızı"]

exampleSpace = [A,B,C,D,E,F]

x = int(input("X Verisini Giriniz:"))
y = int(input("Y Verisini Giriniz:"))

exampleDot = [x,y,""]

def KNNcalculate(space,example,n):
	tmpExampleSpace = space.copy()
	tmpExampleDot = example.copy()
	tmpExampleDot.pop()

	komsular = []
	boyut = len(example)-1    
	print("En yakın '" + str(n) + "' komşu :")

	for i in range(n):        
		enYakinEleman = []
		for j in range(len(tmpExampleSpace)):
			minimumMesafe = 1000
			for eleman in tmpExampleSpace:
				tmp_eleman = eleman.copy()
				tmp_eleman.pop()            
				mesafe = euclideanDistance(tmp_eleman,tmpExampleDot)                                             
				if mesafe <= minimumMesafe:
					minimumMesafe = mesafe
					enYakinEleman = eleman.copy()
		print(enYakinEleman)
		renk =  enYakinEleman[len(enYakinEleman)- 1]
		komsular.append(renk)
		tmpExampleSpace.remove(enYakinEleman)
	print("Komşuların Renkleri :")
	print(komsular)    
	return most_frequent(komsular)

exampleDot_ = KNNcalculate(exampleSpace,exampleDot,3)
print(exampleDot_)