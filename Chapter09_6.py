#List Nilai + Status LULUS atau TIDAK LULUS
listNilai = [{'NIM' : 'A01', 'NAMA' : 'AGUSTINA', 'MID' : 50, 'uas' : 80},
 {'NIM' : 'A02', 'NAMA' : 'BUDI', 'MID' : 40, 'uas' : 90}, 
 {'NIM' : 'A03', 'NAMA' : 'CHICHA', 'MID' : 100, 'uas' : 50},
 {'NIM' : 'A04', 'NAMA' : 'DONNA', 'MID' : 20, 'uas' : 100},
 {'NIM' : 'A05', 'NAMA' : 'FATIMAH', 'MID' : 70, 'uas' : 100}]

print('======================================================================')
print('NIM'.ljust(10) + 'NAMA'.ljust(15) + 'N.MID'.ljust(10) + 'N.UAS'.ljust(10) + 'N.AKHIR'.ljust(14) + 'STATUS'.ljust(10))
i = 0
print('----------------------------------------------------------------------')
for daftar in listNilai :
    Mahasiswa = listNilai[i]
    NIM = Mahasiswa['NIM']
    NAMA = Mahasiswa['NAMA']
    MID = str(Mahasiswa['MID'])
    uas = str(Mahasiswa['uas'])
    akhir = round((Mahasiswa['MID'] + 2*Mahasiswa['uas'])/3)
    status = ''
    if akhir >= 60 :
        status = 'LULUS'
    else:
        status = 'TIDAK LULUS'
    print(NIM.ljust(10) + NAMA.ljust(15) + MID.rjust(5) + uas.rjust(10) + str(akhir).rjust(12) + status.rjust(12))
    i += 1
print('----------------------------------------------------------------------')