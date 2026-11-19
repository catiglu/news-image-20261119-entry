from PIL import Image, ImageDraw, ImageFont
import textwrap

W, H = 1200, 1600
img = Image.new("RGB", (W, H), "#0b1020")
d = ImageDraw.Draw(img)

title = "World News — 19 November 2026"
d.text((60, 60), title, fill="#f5f5f5", font=None)

headlines = [
 "1. UN Security Council holds emergency session on Middle East ceasefire violations.",
 "2. G20 leaders agree on new climate finance framework in Johannesburg.",
 "3. Major earthquake (M7.2) strikes Pacific; tsunami warnings issued.",
 "4. EU announces AI Act enforcement timeline and compliance deadlines.",
 "5. US Federal Reserve signals rate hold amid cooling inflation.",
 "6. China and India resume border talks after months of stalemate.",
 "7. Global oil prices fall on OPEC+ output decision.",
 "8. WHO declares end of mpox emergency in several regions.",
 "9. Tech giants report record quarterly earnings driven by AI demand.",
 "10. COP30 delegates finalize loss-and-damage fund operational rules.",
]

y = 160
for h in headlines:
    for line in textwrap.wrap(h, width=70):
        d.text((60, y), line, fill="#d0d6e0")
        y += 40
    y += 20

img.save("news_summary.png")
print("Saved news_summary.png")
