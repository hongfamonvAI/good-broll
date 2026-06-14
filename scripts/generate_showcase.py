#!/usr/bin/env python3
"""Generate deterministic showcase images for the Good B-roll skill."""

from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "showcase"
W, H = 1080, 1440
MARGIN = 72


FONT_CANDIDATES = [
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    for path in FONT_CANDIDATES:
        try:
            return ImageFont.truetype(path, size=size, index=0)
        except Exception:
            continue
    return ImageFont.load_default()


F_TITLE = font(58, True)
F_SUB = font(30)
F_LABEL = font(28)
F_SMALL = font(24)
F_MONO = font(26)


def save(img: Image.Image, name: str) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    img.save(path, "PNG", optimize=True)
    return path


def text(draw: ImageDraw.ImageDraw, xy, value, fill="#1c1c1c", fnt=None, anchor=None):
    draw.text(xy, value, fill=fill, font=fnt or F_LABEL, anchor=anchor)


def rounded(draw, box, radius=24, fill="#ffffff", outline=None, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def shadow(base: Image.Image, box, radius=28, offset=(0, 12), blur=24, fill=(0, 0, 0, 60)):
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    shifted = tuple(v + offset[i % 2] for i, v in enumerate(box))
    d.rounded_rectangle(shifted, radius=radius, fill=fill)
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    base.alpha_composite(layer)


def header(draw, zh, en, fill="#1c1c1c"):
    text(draw, (MARGIN, 62), zh, fill=fill, fnt=F_TITLE)
    text(draw, (MARGIN, 132), en, fill=fill, fnt=F_SUB)


def paper_texture(img: Image.Image, opacity=18):
    random.seed(7)
    px = img.load()
    for _ in range(18000):
        x = random.randrange(img.width)
        y = random.randrange(img.height)
        r, g, b, a = px[x, y]
        delta = random.randrange(-opacity, opacity + 1)
        px[x, y] = (
            max(0, min(255, r + delta)),
            max(0, min(255, g + delta)),
            max(0, min(255, b + delta)),
            a,
        )


def collage() -> Image.Image:
    img = Image.new("RGBA", (W, H), "#f5f2ea")
    d = ImageDraw.Draw(img)
    paper_texture(img, 9)
    header(d, "社媒拼贴插画风", "Editorial Collage / cut-paper B-roll")

    # cut paper cards
    palettes = ["#8ec5ff", "#c7a4ff", "#ffb26f", "#ff7b8a", "#ffe16a"]
    for i, (x, y, w, h, rot, c) in enumerate(
        [
            (100, 280, 360, 260, -7, palettes[0]),
            (570, 310, 340, 250, 6, palettes[1]),
            (210, 730, 660, 340, -2, "#ffffff"),
        ]
    ):
        card = Image.new("RGBA", (w + 70, h + 70), (0, 0, 0, 0))
        cd = ImageDraw.Draw(card)
        rounded(cd, (28, 28, w + 28, h + 28), 34, c)
        cd.rectangle((68, 16, 158, 48), fill="#f7d68f")
        card = card.rotate(rot, expand=True, resample=Image.Resampling.BICUBIC)
        img.alpha_composite(card, (x, y))

    # two paper characters
    d = ImageDraw.Draw(img)
    d.ellipse((195, 360, 275, 440), fill="#332c2d")
    d.rounded_rectangle((164, 430, 306, 590), 36, fill="#2d5d7b")
    d.polygon([(140, 470), (80, 575), (155, 570)], fill="#2d5d7b")
    d.polygon([(310, 475), (390, 555), (320, 582)], fill="#2d5d7b")
    d.rounded_rectangle((625, 382, 765, 545), 38, fill="#ff7b8a")
    d.ellipse((648, 320, 742, 414), fill="#3a3030")
    d.arc((664, 356, 724, 392), 0, 180, fill="#ffffff", width=5)

    # UI/workflow
    rounded(d, (240, 782, 835, 1025), 30, "#fdfdfb", "#262626", 3)
    for i, x in enumerate([300, 470, 640]):
        rounded(d, (x, 840, x + 120, 920), 22, palettes[i], "#1e1e1e", 3)
        d.line((x + 120, 880, x + 170, 880), fill="#1e1e1e", width=6)
        d.polygon([(x + 170, 880), (x + 150, 866), (x + 150, 894)], fill="#1e1e1e")
    text(d, (298, 970), "</>  +  AI  +  API", fnt=F_MONO)

    for x, y, c in [(150, 1120, "#ffb26f"), (840, 220, "#ff7b8a"), (870, 1060, "#8ec5ff")]:
        d.regular_polygon((x, y, 36), 5, fill=c, outline="#1f1f1f")
    text(d, (MARGIN, 1270), "抽象文案 → 人物 / 道具 / UI / 隐喻", fnt=F_LABEL)
    return img


def handdrawn() -> Image.Image:
    img = Image.new("RGBA", (W, H), "#fff6e8")
    paper_texture(img, 10)
    d = ImageDraw.Draw(img)
    header(d, "温暖手绘插画风", "Warm hand-drawn educational B-roll")
    random.seed(3)

    def wline(points, fill="#5d4b3f", width=5):
        jittered = []
        for x, y in points:
            jittered.append((x + random.randint(-3, 3), y + random.randint(-3, 3)))
        d.line(jittered, fill=fill, width=width, joint="curve")

    rounded(d, (125, 275, 955, 1090), 44, "#fffdf8", "#e5cab2", 4)
    for y in range(360, 1030, 80):
        wline([(180, y), (900, y)], fill="#ead8c9", width=3)

    d.ellipse((232, 445, 340, 553), fill="#ffd6b5", outline="#5d4b3f", width=5)
    d.arc((260, 488, 315, 520), 0, 180, fill="#5d4b3f", width=4)
    d.rounded_rectangle((205, 560, 370, 795), 45, fill="#9cc9b4", outline="#5d4b3f", width=5)
    wline([(380, 665), (515, 605), (655, 650)], width=7)
    rounded(d, (590, 430, 835, 690), 28, "#e8f2ff", "#5d4b3f", 5)
    for y in [488, 535, 582, 629]:
        wline([(630, y), (795, y)], fill="#6e83c6", width=5)

    d.ellipse((690, 770, 790, 870), fill="#ffd6b5", outline="#5d4b3f", width=5)
    d.rounded_rectangle((650, 880, 830, 1040), 44, fill="#f8b0a8", outline="#5d4b3f", width=5)
    rounded(d, (250, 870, 545, 1015), 28, "#fff4bd", "#5d4b3f", 5)
    text(d, (292, 918), "学习路径", fill="#5d4b3f", fnt=F_LABEL)
    text(d, (292, 964), "拆成 3 个镜头", fill="#5d4b3f", fnt=F_SMALL)
    text(d, (MARGIN, 1268), "柔和、亲切，适合教程和经验分享", fill="#5d4b3f", fnt=F_LABEL)
    return img


def cartoon3d() -> Image.Image:
    img = Image.new("RGBA", (W, H), "#dff2ff")
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        r = int(223 * (1 - t) + 255 * t)
        g = int(242 * (1 - t) + 226 * t)
        b = int(255 * (1 - t) + 235 * t)
        d.line((0, y, W, y), fill=(r, g, b, 255))
    header(d, "卡通3D风", "Playful 3D cartoon / soft rounded assets")

    shadow(img, (180, 360, 900, 1005), radius=70, blur=34, fill=(78, 91, 126, 55))
    rounded(d, (180, 360, 900, 1005), 70, "#ffffff", None)
    rounded(d, (260, 650, 820, 930), 48, "#8ec5ff", None)
    rounded(d, (310, 700, 770, 875), 34, "#1f3554", None)
    for i, c in enumerate(["#ffcc66", "#ff7b8a", "#9ee6b2"]):
        d.ellipse((350 + i * 105, 745, 420 + i * 105, 815), fill=c)
    d.ellipse((430, 435, 650, 655), fill="#ffd7bd")
    d.ellipse((382, 392, 702, 545), fill="#59443d")
    d.rounded_rectangle((405, 610, 675, 760), 75, fill="#b795ff")
    d.ellipse((480, 520, 505, 545), fill="#222222")
    d.ellipse((575, 520, 600, 545), fill="#222222")
    d.arc((500, 555, 585, 605), 0, 180, fill="#222222", width=7)
    d.rounded_rectangle((170, 1048, 420, 1160), 42, fill="#ffcf70")
    d.rounded_rectangle((455, 1048, 705, 1160), 42, fill="#91e6b8")
    d.rounded_rectangle((740, 1048, 990, 1160), 42, fill="#ff9db1")
    text(d, (235, 1088), "脚本", fnt=F_LABEL)
    text(d, (520, 1088), "镜头", fnt=F_LABEL)
    text(d, (805, 1088), "素材", fnt=F_LABEL)
    text(d, (MARGIN, 1270), "圆润、轻量，适合活泼工具讲解", fnt=F_LABEL)
    return img


def doodle() -> Image.Image:
    img = Image.new("RGBA", (W, H), "#f8fbf1")
    d = ImageDraw.Draw(img)
    header(d, "白板涂鸦讲解风", "Whiteboard doodle / notebook explainer")
    for x in range(80, W, 72):
        d.line((x, 220, x, 1180), fill="#dfe9d8", width=2)
    for y in range(240, 1180, 72):
        d.line((60, y, 1020, y), fill="#dfe9d8", width=2)
    random.seed(10)

    def scribble(points, width=5, fill="#1a1a1a"):
        for _ in range(2):
            d.line(
                [(x + random.randint(-4, 4), y + random.randint(-4, 4)) for x, y in points],
                fill=fill,
                width=width,
                joint="curve",
            )

    d.ellipse((195, 438, 285, 528), outline="#1a1a1a", width=6)
    scribble([(240, 528), (240, 760)])
    scribble([(240, 595), (150, 670)])
    scribble([(240, 595), (360, 655)])
    scribble([(240, 760), (180, 910)])
    scribble([(240, 760), (315, 910)])
    rounded(d, (520, 390, 885, 600), 18, "#ffffff", "#1a1a1a", 5)
    scribble([(560, 460), (820, 460)])
    scribble([(560, 520), (760, 520)])
    rounded(d, (520, 740, 885, 960), 18, "#ffffff", "#1a1a1a", 5)
    scribble([(565, 815), (795, 815)])
    scribble([(565, 875), (830, 875)])
    d.polygon([(432, 645), (480, 620), (480, 670)], fill="#ffeb66", outline="#1a1a1a")
    scribble([(370, 646), (480, 646)], width=7)
    d.rectangle((365, 1045, 715, 1112), fill=(255, 238, 88, 135))
    text(d, (390, 1058), "讲清楚：是什么 → 怎么做", fnt=F_LABEL)
    text(d, (MARGIN, 1270), "随手画、箭头和高亮，适合逻辑拆解", fnt=F_LABEL)
    return img


def warm_sketch() -> Image.Image:
    img = Image.new("RGBA", (W, H), "#f5f0e8")
    paper_texture(img, 8)
    d = ImageDraw.Draw(img)
    header(d, "暖纸黑线产品草图风", "Warm sketch explainer / lo-fi SaaS drawing")
    random.seed(18)

    def rough_line(points, width=7):
        for _ in range(2):
            d.line(
                [(x + random.randint(-3, 3), y + random.randint(-3, 3)) for x, y in points],
                fill="#161616",
                width=width,
                joint="curve",
            )

    rounded(d, (210, 360, 820, 880), 34, "#ffffff", "#161616", 7)
    rough_line([(260, 450), (760, 450)], 5)
    rough_line([(260, 540), (595, 540)], 5)
    rough_line([(260, 630), (700, 630)], 5)
    rounded(d, (110, 810, 430, 1040), 28, "#ffffff", "#161616", 7)
    rounded(d, (650, 780, 955, 1060), 28, "#ffffff", "#161616", 7)
    rough_line([(430, 920), (650, 900)], 8)
    d.polygon([(650, 900), (620, 880), (625, 925)], fill="#161616")
    d.ellipse((310, 980, 385, 1055), outline="#161616", width=7)
    rough_line([(350, 1055), (350, 1160)], 7)
    rough_line([(350, 1098), (260, 1142)], 7)
    rough_line([(350, 1098), (460, 1130)], 7)
    text(d, (145, 860), "输入", fnt=F_LABEL)
    text(d, (700, 835), "输出", fnt=F_LABEL)
    text(d, (270, 392), "核心界面", fnt=F_LABEL)
    text(d, (MARGIN, 1270), "白色信息层 + 粗黑线条 + 清晰主次", fnt=F_LABEL)
    return img


def make_showcase(paths):
    title_h = 190
    gap = 42
    scale_w = 900
    thumb_h = int(H * scale_w / W)
    out_h = title_h + len(paths) * thumb_h + (len(paths) + 1) * gap
    sheet = Image.new("RGBA", (1080, out_h), "#111111")
    d = ImageDraw.Draw(sheet)
    text(d, (72, 54), "Good B-roll Skill", fill="#ffffff", fnt=F_TITLE)
    text(d, (72, 128), "5 visual styles for turning scripts into B-roll prompts", fill="#d6d6d6", fnt=F_SUB)
    y = title_h + gap
    for path in paths:
        im = Image.open(path).convert("RGBA").resize((scale_w, thumb_h), Image.Resampling.LANCZOS)
        shadow(sheet, (90, y, 90 + scale_w, y + thumb_h), radius=24, blur=20, fill=(0, 0, 0, 90))
        sheet.alpha_composite(im, (90, y))
        y += thumb_h + gap
    save(sheet, "good-broll-showcase.png")


def main():
    items = [
        ("editorial-collage.png", collage()),
        ("warm-handdrawn.png", handdrawn()),
        ("playful-3d-cartoon.png", cartoon3d()),
        ("whiteboard-doodle.png", doodle()),
        ("warm-sketch-explainer.png", warm_sketch()),
    ]
    paths = [save(img, name) for name, img in items]
    make_showcase(paths)
    for path in paths + [OUT / "good-broll-showcase.png"]:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
