menu = {
    "Nasi goreng" : 12000,
    "Mie ayam" : 10000,
    "Es teh" : 3000,
    "Teh anget" : 2500,
    "Mi goreng" : 13000
}



def tampil_menu(menu):
    print(f"{'Daftar Menu':^20}")
    for item,harga in menu.items():
        print(f"{item}: Rp. {harga}")

def tambah_ke_keranjang(keranjang, menu,item,jumlah):
    if item not in menu:
        print("Item tidak ada")
        return
    harga = menu[item]
    if item in keranjang:
        keranjang[item]["jumlah"]+= jumlah
    else:
        keranjang[item]= {"harga": harga,"jumlah": jumlah}
    print(f"{jumlah}{item} Berhasil ditambahkan")

def hitung_total(keranjang):
    total = 0
    for item,detail in keranjang.items():
        total += detail["harga"]*detail["jumlah"]
    return total
def struk(keranjang):
    if not keranjang:
        print("Kosong")
        if x== True: 
            input("kembali Ke menu (Enter) ")
            print("")
            return
    for item,detail in keranjang.items():
        print(f"{item} x {detail["jumlah"]}: Rp. {detail["harga"]* detail["jumlah"]}")

    total = hitung_total(keranjang)
    print("-"*20)
    print(f"Total : {total}" )
    if x== True: 
        input("kembali Ke menu (Enter) ")
        print("")

keranjang ={}
x =True
while x ==True:
    print(f"{'Sistem kasir':^20}")
    tampil_menu(menu)
    print("------------------------")
    print("1. Tambah ke Keranjang")
    print("2. Tampilkan Struk")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        ulangi = "y"
        while ulangi=="y":
            item = input("Masukkan nama item: ")
            jumlah = int(input("Masukkan jumlah: "))
            tambah_ke_keranjang(keranjang, menu, item, jumlah)

            ulangi = input("Tambah lagi (y/n)?")
            if ulangi =="n":
                break
    elif pilihan == "2":
        struk(keranjang)
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid.")

    # x = input("ulangi ? (y/n)")
    # if x =="n":
    #     break
