angka_win = 9 
hitung = 0 
limit = 2
while hitung < limit:
    main = int(input('game:'))
    hitung += 1

    if main == angka_win:
        print('anda menang!')
        break
    else:
        print('anda kalah')