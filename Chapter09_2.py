#Fofmasi Bintang Piramida
def bintang(n):
    a = -1
    b = n
    count = 0
    panjang = 1 + 2*(n-1)
    panjang += panjang
    jarak = ' '
    while count < b :
        a += 2
        count += 1
        piramidabintang = '* '*a
        print(piramidabintang.center(panjang, jarak))

bintang(4)