from PIL import Image
filen = r'icono.jpg'
img = Image.open(filen)
img.save('icon.ico',format = 'ICO', sizes=[(32,32)])