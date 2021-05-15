from PIL import Image

def make_preview(size, n_colors):
    im = Image.open("imag2.jpg")
    out = im.resize(size)
    out = out.quantize(n_colors)
    out.save('res.bmp')
make_preview((400, 200),64)