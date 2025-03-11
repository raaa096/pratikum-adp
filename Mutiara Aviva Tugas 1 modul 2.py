def tampilkan_film():
    print('========== Daftar Film ===========')
    print(f'1 = captain america     Rp 50000')
    print(f'2 = keluarga cemara     Rp 40000')
    print(f'3 = doraemon the movie  Rp 45000')
    print(f'4 = naruto the movie    Rp 45000') 
    print(f'5 = moana 2             Rp 45000')
    print('==================================')

def hitung_diskon(total):
    if total > 250000 :
        return total*0.35
    elif total > 100000 :
        return total*0.15
    else :
        return 0
    
def proses_pemesanan() :
    print('Pembelian tiket bioskop')
    nama = input('Nama : ')

    tampilkan_film()

    kode_film = int(input('Pilih kode film (1-5) : '))
    jumlah_tiket = int(input('Jumlah tiket : '))

    harga = 0
    judul = ""

    if kode_film == 1 :
        judul = "Captain America"
        harga = 50000
    elif kode_film == 2 :
        judul = 'Keluarga Cemara'
        harga = 40000
    elif kode_film == 3 :
        judul = 'Moana 2'
        harga = 45000
    elif kode_film == 4 :
        judul = 'Doraemon the movie'
        harga = 45000
    elif kode_film == 5 :
        judul = 'Naruto the movie'
        harga = 45000
    else :
        print('Kode film tidak tersedia')
        return

    total_harga = harga*jumlah_tiket
    diskon = hitung_diskon (total_harga)
    total_bayar = total_harga - diskon

    print('========= Struk Pemesanan Tiket =========')
    print(f'Nama           : {nama}')
    print(f'Judul Film     : {judul}')
    print(f'Jumlah Tiket   : {jumlah_tiket}')
    print(f'Harga Satuan   : {harga}')
    print(f'Potongan Harga : {diskon}')
    print(f'Total Harga    : {total_bayar}')
    print('=========================================')
    
proses_pemesanan()