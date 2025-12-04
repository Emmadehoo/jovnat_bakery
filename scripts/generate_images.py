"""
Generate placeholder JPEG and WebP images for the Jovnat project.
Creates images in ../images/ with multiple sizes for hero and product thumbnails.
Requires: Pillow
Run: python scripts/generate_images.py
"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'images')
os.makedirs(OUT_DIR, exist_ok=True)

# simple font fallback: try to use a truetype font, else default
try:
    FONT = ImageFont.truetype('arial.ttf', 40)
except Exception:
    try:
        FONT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 40)
    except Exception:
        FONT = ImageFont.load_default()


def make_image(name, size, bg, text, path):
    img = Image.new('RGB', size, bg)
    draw = ImageDraw.Draw(img)
    # measure text using textbbox for compatibility
    bbox = draw.textbbox((0,0), text, font=FONT)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    draw.text(((size[0]-w)/2, (size[1]-h)/2), text, fill=(255,255,255), font=FONT)
    img.save(path, quality=90)


def generate():
    hero_sizes = [(480,320),(800,533),(1200,800)]
    product_sizes = [(320,220),(640,440)]

    # hero
    for (w,h) in hero_sizes:
        base = os.path.join(OUT_DIR, f'hero-{w}x{h}.jpg')
        make_image('hero', (w,h), (184,91,42), 'Jovnat Bakery', base)
        # webp
        webp = os.path.splitext(base)[0]+'.webp'
        Image.open(base).save(webp, 'WEBP', quality=85)

    # products
    products = [('sourdough','Sourdough Loaf'),('croissant','Butter Croissant'),('cake','Seasonal Cake')]
    for slug, title in products:
        for (w,h) in product_sizes:
            base = os.path.join(OUT_DIR, f'{slug}-{w}x{h}.jpg')
            make_image(slug, (w,h), (244,162,97), title, base)
            webp = os.path.splitext(base)[0]+'.webp'
            Image.open(base).save(webp, 'WEBP', quality=85)

    print('Generated images in', OUT_DIR)

if __name__ == '__main__':
    generate()
