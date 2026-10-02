import os
from PIL import Image, ImageDraw, ImageFont

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
THUMBNAIL_PATH = os.path.join(CURRENT_DIR, "thumbnail.jpg")

WIDTH = 1080
HEIGHT = 1920

# Fonts
FONT_BOLD = "C:/Windows/Fonts/seguibl.ttf"
if not os.path.exists(FONT_BOLD):
    FONT_BOLD = "C:/Windows/Fonts/arialbd.ttf"

font_title_lg = ImageFont.truetype(FONT_BOLD, 76)
font_title_md = ImageFont.truetype(FONT_BOLD, 54)
font_pill = ImageFont.truetype(FONT_BOLD, 30)
font_word = ImageFont.truetype(FONT_BOLD, 52)
font_token = ImageFont.truetype(FONT_BOLD, 44)
font_token_sub = ImageFont.truetype(FONT_BOLD, 26)
font_ai_resp = ImageFont.truetype(FONT_BOLD, 38)
font_bottom = ImageFont.truetype(FONT_BOLD, 34)

# Colors
BG_COLOR = (11, 15, 25) # Obsidian #0B0F19
CARD_BG = (18, 24, 38)
CYAN = (0, 240, 255)
MINT = (0, 255, 163)
GOLD = (255, 215, 0)
CRIMSON = (255, 51, 102)
WHITE = (255, 255, 255)
SLATE = (136, 146, 176)
DARK_RED = (35, 15, 22)
DARK_BLUE = (15, 36, 58)
DARK_GREEN = (13, 46, 38)

im = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
draw = ImageDraw.Draw(im)

# Subtle background glow/accents
for r in range(400, 0, -20):
    alpha = int(8 * (1 - r / 400))
    draw.ellipse([540 - r, 700 - r, 540 + r, 700 + r], fill=(15, 25, 45))

# 1. TOP CATEGORY PILL (Y=240)
pill_text = "AI REASONING FLAW 🍓"
bbox = font_pill.getbbox(pill_text)
pw = bbox[2] - bbox[0]
ph = bbox[3] - bbox[1]
px = (WIDTH - pw) // 2
py = 240
draw.rounded_rectangle([px - 28, py - 12, px + pw + 28, py + ph + 12], radius=16, fill=CARD_BG, outline=SLATE, width=2)
draw.text((px, py - bbox[1]), pill_text, font=font_pill, fill=GOLD)

# 2. MAIN HOOK TITLE (Y=340)
t1 = "WHY CAN'T AI"
b1 = font_title_lg.getbbox(t1)
w1 = b1[2] - b1[0]
draw.text(((WIDTH - w1) // 2, 340 - b1[1]), t1, font=font_title_lg, fill=WHITE)

t2 = "COUNT TO 3?"
b2 = font_title_lg.getbbox(t2)
w2 = b2[2] - b2[0]
draw.text(((WIDTH - w2) // 2, 450 - b2[1]), t2, font=font_title_lg, fill=CRIMSON)

# 3. EXHIBIT CARD: THE WORD STRAWBERRY (Y=620)
card_w = 920
card_h = 240
cx = (WIDTH - card_w) // 2
cy = 600
draw.rounded_rectangle([cx, cy, cx + card_w, cy + card_h], radius=24, fill=CARD_BG, outline=CYAN, width=3)

# Subtitle above letters
sub_lbl = "HOW MANY 'R's IN STRAWBERRY?"
b_sub = font_pill.getbbox(sub_lbl)
draw.text(((WIDTH - (b_sub[2]-b_sub[0])) // 2, cy + 30 - b_sub[1]), sub_lbl, font=font_pill, fill=SLATE)

# Colored letters
letters = [
    ("S", WHITE), ("T", WHITE), ("R", GOLD), ("A", WHITE), ("W", WHITE),
    ("B", WHITE), ("E", WHITE), ("R", GOLD), ("R", GOLD), ("Y", WHITE)
]
# Calculate total width
spacing = 30
letter_widths = [font_word.getbbox(ch)[2] - font_word.getbbox(ch)[0] for ch, _ in letters]
total_word_w = sum(letter_widths) + spacing * (len(letters) - 1)
cur_x = (WIDTH - total_word_w) // 2
letter_y = cy + 120

for ch, col in letters:
    bb = font_word.getbbox(ch)
    draw.text((cur_x, letter_y - bb[1]), ch, font=font_word, fill=col)
    cur_x += (bb[2] - bb[0]) + spacing

# 4. AI FAIL RESPONSE CARD (Y=900)
fail_w = 920
fail_h = 160
fx = (WIDTH - fail_w) // 2
fy = 890
draw.rounded_rectangle([fx, fy, fx + fail_w, fy + fail_h], radius=20, fill=DARK_RED, outline=CRIMSON, width=3)
resp_txt = "AI ANSWER: \"THERE ARE 2 R's\" ✗"
b_resp = font_ai_resp.getbbox(resp_txt)
draw.text(((WIDTH - (b_resp[2]-b_resp[0])) // 2, fy + 58 - b_resp[1]), resp_txt, font=font_ai_resp, fill=CRIMSON)

# 5. THE REALITY: TOKEN CHUNKS CARD (Y=1110)
tok_card_w = 920
tok_card_h = 300
tx = (WIDTH - tok_card_w) // 2
ty = 1100
draw.rounded_rectangle([tx, ty, tx + tok_card_w, ty + tok_card_h], radius=24, fill=CARD_BG, outline=GOLD, width=3)

tok_lbl = "WHAT THE AI ACTUALLY SEES:"
b_tl = font_pill.getbbox(tok_lbl)
draw.text(((WIDTH - (b_tl[2]-b_tl[0])) // 2, ty + 30 - b_tl[1]), tok_lbl, font=font_pill, fill=GOLD)

# Two token blocks side by side
b_w = 380
b_h = 160
b1_x = tx + 50
b2_x = tx + tok_card_w - b_w - 50
b_y = ty + 95

# Token 1: straw
draw.rounded_rectangle([b1_x, b_y, b1_x + b_w, b_y + b_h], radius=16, fill=DARK_BLUE, outline=CYAN, width=3)
t_t1 = "straw"
b_t1 = font_token.getbbox(t_t1)
draw.text((b1_x + (b_w - (b_t1[2]-b_t1[0])) // 2, b_y + 40 - b_t1[1]), t_t1, font=font_token, fill=CYAN)
sub1 = "Token ID: 496"
b_s1 = font_token_sub.getbbox(sub1)
draw.text((b1_x + (b_w - (b_s1[2]-b_s1[0])) // 2, b_y + 110 - b_s1[1]), sub1, font=font_token_sub, fill=SLATE)

# Token 2: berry
draw.rounded_rectangle([b2_x, b_y, b2_x + b_w, b_y + b_h], radius=16, fill=DARK_GREEN, outline=MINT, width=3)
t_t2 = "berry"
b_t2 = font_token.getbbox(t_t2)
draw.text((b2_x + (b_w - (b_t2[2]-b_t2[0])) // 2, b_y + 40 - b_t2[1]), t_t2, font=font_token, fill=MINT)
sub2 = "Token ID: 675"
b_s2 = font_token_sub.getbbox(sub2)
draw.text((b2_x + (b_w - (b_s2[2]-b_s2[0])) // 2, b_y + 110 - b_s2[1]), sub2, font=font_token_sub, fill=SLATE)

# 6. BOTTOM BANNER: THE BLIND SPOT (Y=1470)
bot_w = 920
bot_h = 160
bx = (WIDTH - bot_w) // 2
by = 1460
draw.rounded_rectangle([bx, by, bx + bot_w, by + bot_h], radius=20, fill=(24, 19, 36), outline=CYAN, width=3)

bot_t1 = "THE TOKENIZER BLIND SPOT"
b_bt1 = font_bottom.getbbox(bot_t1)
draw.text(((WIDTH - (b_bt1[2]-b_bt1[0])) // 2, by + 40 - b_bt1[1]), bot_t1, font=font_bottom, fill=CYAN)

bot_t2 = "ZERO LETTERS VISIBLE INSIDE"
b_bt2 = font_pill.getbbox(bot_t2)
draw.text(((WIDTH - (b_bt2[2]-b_bt2[0])) // 2, by + 98 - b_bt2[1]), bot_t2, font=font_pill, fill=WHITE)

# 7. CHANNEL FOOTER (Y=1730)
ch_text = "QUANTROVE  •  AI & ML IN THE REAL WORLD"
b_ch = font_pill.getbbox(ch_text)
draw.text(((WIDTH - (b_ch[2]-b_ch[0])) // 2, 1730 - b_ch[1]), ch_text, font=font_pill, fill=SLATE)

im.save(THUMBNAIL_PATH, "JPEG", quality=95)
print(f"✅ Thumbnail created successfully at: {THUMBNAIL_PATH}")
