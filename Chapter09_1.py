#Methode menggunakan looping
def ubahHuruf(teks, a, b):
	    teks = list(teks)
	    result = []
	    for huruf in teks:
	        if huruf == a :
	            huruf = b
	        result.append(huruf)
	    print(''.join(result))

ubahHuruf('MATEMATIKA', 'T', 'S')


#Alternatif Menggunakan Replace
def ubahHuruf2(teks, a, b):
    print(teks.replace(a, b))


ubahHuruf2('MATEMATIKA', 'T', 'S')