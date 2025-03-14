M = float(input('Masukkan modal awal : '))
r = float(input('Masukkan suku bunga tahunan (%) : '))
T = float(input('Masukkan target investasi : '))
tahun= 0
while M<T :
    tahun+=1
    M += M*(r/100) 
    print(f'Tahun ke-{tahun}: Rp {M}')
print(f'Target tercapai dalam {tahun} tahun !')
