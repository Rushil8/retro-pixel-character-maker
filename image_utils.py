from PIL import Image

PALETTES ={
    "gameboy":[(15,56,15),(48,98,48),(139,172,15),(155,188,15)],
    "nes":[(124,124,124),(0,0,252),(0,168,0),(252,252,252)]
}

def center_crop_square(img):
    w,h = img.size
    size = min(w,h)
    left = (w-size)//2
    top=(h-size)//2
    return img.crop((left,top,left+size,top+size))

def apply_palette(img,palette):
    pal_img = Image.new("P", (1,1))
    pal=[]
    for color in palette:
        pal.extend(color)
    pal += [0] * (768 - len(pal))
    pal_img.putpalette(pal)
    img = img.convert("RGB")
    return img.quantize(palette=pal_img,dither=Image.NONE)

def pixelate(img, pixel_size=16, palette_size=16,palette_type="default"):
    img = center_crop_square(img)
    img = img.resize((256,256), Image.BILINEAR)

    img_small = img.resize(
        (256// pixel_size,256// pixel_size),
        Image.BILINEAR
    )

    if palette_type in PALETTES:
        img_small = apply_palette(img_small, PALETTES[palette_type])
    else:
        img_small = img_small.quantize(colors=palette_size,method=2)
    
    img_pixel = img_small.resize((256,256), Image.NEAREST)
    return img_pixel