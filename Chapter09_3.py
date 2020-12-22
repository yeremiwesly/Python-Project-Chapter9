#Fofmasi Belah Ketupat
def bintang(n):
    a = -1
    b = round(n / 2)
    count = 0
    panjang = 1 + 2*(n-1)
    panjang += panjang
    jarak = ' '
    while count < b :
        a += 2
        count += 1
        belahketupat = '* '*a
        print(belahketupat.center(panjang, jarak))
    
    while count >- b :
        a -= 2
        count -= 1
        belahketupat = '* '*a
        print(belahketupat.center(panjang, jarak))
        if(count == 1):
            break

bintang(7)