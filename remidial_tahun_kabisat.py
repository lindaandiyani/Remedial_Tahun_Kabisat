
def Kabisat():
    tahun = int(input('ketikkan tahun : '))
    if tahun%400 == 0:
        chek = 'termasuk TAHUN KABISAT'
    else:
        if tahun%100 == 0:
            chek = 'BUKAN termasuk TAHUN KABISAT'
        else:
            if tahun%4 == 0:
                chek = 'termasuk TAHUN KABISAT'
            else:
                chek = 'BUKAN termasuk TAHUN KABISAT'
    print(f'Hasil : {chek}')
    return chek

Kabisat()

