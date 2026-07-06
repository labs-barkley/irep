"""IREP favicon set - monogram 'IR' on cream, ink type, green signature underline.
Outputs into docs/ (site root files). Run from repo root: python make_favicons.py"""
from PIL import Image, ImageDraw, ImageFont

PAPER=(250,247,241,255); INK=(27,42,65,255); GREEN=(0,120,92,255)

def make(size):
    im = Image.new("RGBA",(size,size),PAPER)
    d = ImageDraw.Draw(im)
    try:
        f = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", int(size*0.62))
    except Exception:
        f = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", int(size*0.60))
    t="IR"
    bb=d.textbbox((0,0),t,font=f)
    w,h=bb[2]-bb[0],bb[3]-bb[1]
    x=(size-w)/2-bb[0]; y=(size-h)/2-bb[1]-size*0.06
    d.text((x,y),t,font=f,fill=INK)
    # green signature underline
    uy=int(size*0.80); uh=max(2,int(size*0.06))
    ux0=int(size*0.20); ux1=int(size*0.80)
    d.rectangle([ux0,uy,ux1,uy+uh],fill=GREEN)
    return im

sizes={16:"docs/favicon-16.png",32:"docs/favicon-32.png",180:"docs/apple-touch-icon.png",192:"docs/icon-192.png",512:"docs/icon-512.png"}
imgs={}
for s,p in sizes.items():
    im=make(s); im.save(p); imgs[s]=im
imgs[32].save("docs/favicon.ico", sizes=[(16,16),(32,32),(48,48)])
print("favicons written:", ", ".join(sizes.values()), "+ docs/favicon.ico")
