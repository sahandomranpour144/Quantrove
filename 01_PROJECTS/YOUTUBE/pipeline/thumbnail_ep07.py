"""EP07 thumbnail, concept A (1280x720, palette lock). Usage: python thumbnail_ep07.py <out.png>"""
import math, os, random, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

BG, SLATE, LIME, PUMPKIN, TEXT = "#202322", "#233D4C", "#C3D809", "#FD802E", "#E6EDF3"
FONT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "assets", "fonts", "Nohemi-Bold.ttf")
W, H = 1280, 720

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
for x in range(0, W, 64):                       # faint grid
    d.line([(x, 0), (x, H)], fill="#222b2c", width=1)
for y in range(0, H, 64):
    d.line([(0, y), (W, y)], fill="#222b2c", width=1)

rng = random.Random(7)                          # constellation, right 60% of frame
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
g = ImageDraw.Draw(glow)
for _ in range(420):
    x, y = rng.gauss(900, 190), rng.gauss(400, 130)
    r = rng.uniform(1.5, 4.0)
    col = LIME if rng.random() < 0.3 else TEXT
    g.ellipse([x - r, y - r, x + r, y + r], fill=col + "%02x" % rng.randint(60, 200))
img.paste(glow, (0, 0), glow)

man, woman = (700, 560), (720, 330)            # KING - MAN + WOMAN = QUEEN, parallel arrows
king = (1010, 540)
queen = (king[0] + woman[0] - man[0], king[1] + woman[1] - man[1])
halo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
hd = ImageDraw.Draw(halo)
for r, a in [(70, 40), (44, 80)]:
    hd.ellipse([queen[0] - r, queen[1] - r, queen[0] + r, queen[1] + r], fill=(195, 216, 9, a))
img.paste(halo.filter(ImageFilter.GaussianBlur(14)), (0, 0), halo.filter(ImageFilter.GaussianBlur(14)))
d = ImageDraw.Draw(img)

def arrow(p, q, color, w):
    d.line([p, q], fill=color, width=w)
    ang = math.atan2(q[1] - p[1], q[0] - p[0])
    for s in (2.6, -2.6):
        d.line([q, (q[0] + 34 * math.cos(ang + s), q[1] + 34 * math.sin(ang + s))], fill=color, width=w)

arrow(man, woman, TEXT, 5)
arrow(king, queen, LIME, 9)
f_lab, f_eq, f_q = (ImageFont.truetype(FONT, s) for s in (34, 76, 170))
for (x, y), t, c in [(man, "MAN", TEXT), (woman, "WOMAN", TEXT), (king, "KING", TEXT)]:
    d.ellipse([x - 9, y - 9, x + 9, y + 9], fill=c)
    d.text((x + 18, y - 18), t, font=f_lab, fill=c)
d.ellipse([queen[0] - 16, queen[1] - 16, queen[0] + 16, queen[1] + 16], fill=LIME)
# no QUEEN label: the glowing point IS the question (keeps the "= ?" curiosity gap)

d.text((64, 70), "KING − MAN", font=f_eq, fill=TEXT)   # text block, left
d.text((64, 165), "+ WOMAN", font=f_eq, fill=TEXT)
d.text((56, 250), "= ?", font=f_q, fill=LIME)
img.save(sys.argv[1])
print("saved", sys.argv[1])
