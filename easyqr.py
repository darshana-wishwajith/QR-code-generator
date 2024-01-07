import qrcode
exit = False
while not(exit) :
    def qr_code_generator(data, bd, bs, fc, bc, name) :

        qr = qrcode.QRCode(border = bd, box_size = bs)
        qr.add_data(data)
        qr.make(fit = True)
        img = qr.make_image(fill_color = fc, back_color = bc)
        if not(name[-4 : ] == ".png") :
            name = name + ".png"
        img.save("outputs/" + name)
        print(f"\nYour -> 'outputs/{name}' <- QR cod has been generated successfully!")

    print("---------- E A S Y  Q R ---------- (++++ Developer - Darshana Wishwajith ++++ 19/10/2022)\n")
    data = input("data (URL) for qr code : ")
    try : 
        bd = int(input("Border : "))
        bs = int(input("Box Size : "))
    except :
        bd = 4
        bs = 10

    fc = input("Fill color :")
    bc = input("Background color :")
    name = input("name for qr : ")

    if data == '' :
        data = "https://www.infodarshana.me"
    if bd == '':
        bd = 4
    if bs == '':
        bs = 10
    if fc == '':
        fc = "black"
    if bc == '':
        bc = "white"
    if name == '':
        name = "infodarshana_me.png"

    qr_code_generator(data, bd, bs, fc, bc, name)

    ask = input("\nDo you want generate another qr code ? (y or n) : ")
    if ask == "y" :
        exit = False
    elif ask == "n" :
        exit = True



