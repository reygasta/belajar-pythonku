nama = input('namau? ')
print(nama)
if len(nama) < 4:
    print("minimal nama 4 karakter!")
elif len(nama) > 35:
    print("maksimal nama 35 karakter")
else:
    print("keren namamu!")
