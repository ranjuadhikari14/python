import qrcode
name=input("enter your name:")
img=qrcode.make("name")
type(img)
img.save(f"{name}.png")