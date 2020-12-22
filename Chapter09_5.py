#List Nilai MID dan UAS
listNilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
 {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
 {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
 {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
 {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('====================================================')
print('NIM'.ljust(10) + 'NAMA'.ljust(15) + 'N.MID'.ljust(10) + 'N.UAS'.ljust(10))
i = 0
print('----------------------------------------------------')

for daftar in listNilai :
    Mahasiswa = listNilai[i]
    nim = Mahasiswa['nim']
    nama = Mahasiswa['nama']
    mid = str(Mahasiswa['mid'])
    uas = str(Mahasiswa['uas'])
    print(nim.ljust(10) + nama.ljust(15) + mid.rjust(5) + uas.rjust(10))
    i += 1
print('____________________________________________________')
