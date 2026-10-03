"""EP08 thumbnails (1280x720, palette lock). Usage: python thumbnail_ep08.py <A|B> <out.png>
A (primary): huge lime "2017" + blank paper page; one lime word fans attention lines to every other word.
B (Test & Compare variant): G P T, the T glows lime and becomes a stack of attention blocks."""
import math, os, random, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

BG, SLATE, LIME, PUMPKIN, TEXT = "#202322", "#233D4C", "#C3D809", "#FD802E", "#E6EDF3"
FONT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "assets", "fonts", "Nohemi-Bold.ttf")
W, H = 1280, 720
LIME_RGB, TEXT_RGB = (195, 216, 9), (230, 237, 243)


def base():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    for x in range(0, W, 64):
        d.line([(x, 0), (x, H)], fill="#222b2c", width=1)
    for y in range(0, H, 64):
        d.line([(0, y), (W, y)], fill="#222b2c", width=1)
    return img


def glow_text(img, xy, text, font, color_rgb, blur=18, alpha=150):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(layer).text(xy, text, font=font, fill=color_rgb + (alpha,))
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    img.paste(layer, (0, 0), layer)
    ImageDraw.Draw(img).text(xy, text, font=font, fill=color_rgb)


def bezier(p, q, h, n=40):
    c = ((p[0] + q[0]) / 2, min(p[1], q[1]) - h)
    return [((1 - t) ** 2 * p[0] + 2 * (1 - t) * t * c[0] + t * t * q[0],
             (1 - t) ** 2 * p[1] + 2 * (1 - t) * t * c[1] + t * t * q[1]) for t in (i / n for i in range(n + 1))]


def concept_a():
    img = base()
    pw, ph = 560, 640
    page = Image.new("RGBA", (pw + 80, ph + 80), (0, 0, 0, 0))
    pd = ImageDraw.Draw(page)
    pd.rounded_rectangle([40, 40, 40 + pw, 40 + ph], radius=14, fill=(32, 35, 34, 255), outline=TEXT_RGB + (230,), width=5)
    pd.rectangle([90, 86, 90 + 300, 104], fill=TEXT_RGB + (200,))          # title bar (no real text)
    pd.rectangle([90, 120, 90 + 190, 132], fill=(35, 61, 76, 255))
    rng = random.Random(8)
    bars, y = [], 178
    for row in range(10):
        x = 90
        while x < 40 + pw - 80:
            w = rng.choice([44, 60, 76, 96, 120])
            if x + w > 40 + pw - 50:
                break
            bars.append((x, y, w))
            x += w + 16
        y += 50
    src = next(b for b in bars if b[1] == 178 + 50 * 6 and b[0] > 200)        # the attending word
    tgt = next(b for b in bars if b[1] == 178 + 50 * 2 and b[0] < 200)        # the strongest link
    lines = Image.new("RGBA", page.size, (0, 0, 0, 0))
    ld = ImageDraw.Draw(lines)
    src = (src[0] - 10, src[1] - 4, src[2] + 40)                              # the attending word, drawn larger
    bars = [b for b in bars if not (b[1] == src[1] + 4 and b[0] < src[0] + src[2] + 16 and b[0] + b[2] > src[0] - 16)] + [src]
    sp = (src[0] + src[2] / 2, src[1] + 11)
    for b in bars:
        if b is src:
            continue
        tp = (b[0] + b[2] / 2, b[1] + 6)
        strong = b is tgt
        a = 255 if strong else rng.randint(70, 150)
        ld.line([sp, tp], fill=LIME_RGB + (a,), width=10 if strong else rng.choice([2, 3, 3]))
    halo = Image.new("RGBA", page.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).ellipse([sp[0] - 110, sp[1] - 70, sp[0] + 110, sp[1] + 70], fill=LIME_RGB + (140,))
    halo = halo.filter(ImageFilter.GaussianBlur(28))
    page = Image.alpha_composite(Image.alpha_composite(page, halo), lines)    # page -> glow -> lines -> word bars
    pd = ImageDraw.Draw(page)
    for b in bars:
        col = LIME_RGB + (255,) if b in (src, tgt) else (35, 61, 76, 255)
        pd.rounded_rectangle([b[0], b[1], b[0] + b[2], b[1] + (22 if b is src else 14)], radius=5, fill=col)
    page = page.rotate(-5, resample=Image.BICUBIC, expand=True)
    img.paste(page, (600, -30), page)
    f = ImageFont.truetype(FONT, 250)
    glow_text(img, (36, 205), "2017", f, LIME_RGB, blur=26, alpha=170)
    return img


def concept_b():
    img = base()
    f = ImageFont.truetype(FONT, 330)
    d = ImageDraw.Draw(img)
    d.text((40, 150), "G", font=f, fill=TEXT)
    d.text((320, 150), "P", font=f, fill=TEXT)
    glow_text(img, (580, 150), "T", f, LIME_RGB, blur=30, alpha=200)
    d = ImageDraw.Draw(img)
    # stack of 6 blocks growing out of the T, with an attention web across them
    x0, y0, bw, bh, gap = 830, 110, 360, 70, 16
    blocks = [(x0, y0 + k * (bh + gap)) for k in range(6)]
    web = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    wd = ImageDraw.Draw(web)
    rng = random.Random(3)
    nodes = [(x0 + 40 + i * 70, y + bh / 2) for (_, y) in blocks for i in range(5)]
    for p in nodes:
        for q in rng.sample(nodes, 4):
            if abs(q[1] - p[1]) == bh + gap:                                  # only links between neighbouring layers
                wd.line([p, q], fill=LIME_RGB + (rng.randint(70, 140),), width=2)
    for (x, y) in blocks:
        d.rounded_rectangle([x, y, x + bw, y + bh], radius=10, fill=BG, outline=SLATE, width=4)
        d.rounded_rectangle([x + 14, y + 10, x + bw - 14, y + 30], radius=6, outline=LIME, width=3)
        d.rounded_rectangle([x + 14, y + 40, x + bw - 14, y + 60], radius=6, outline=TEXT, width=3)
    img.paste(web, (0, 0), web)
    d = ImageDraw.Draw(img)
    for (x, y) in nodes:
        d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=LIME)
    d.line([(785, 190), (x0, 190)], fill=LIME, width=8)                     # T crossbar flows into the stack
    return img


if __name__ == "__main__":
    (concept_a if sys.argv[1].upper() == "A" else concept_b)().save(sys.argv[2])
    print("saved", sys.argv[2])
