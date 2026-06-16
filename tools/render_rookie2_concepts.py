from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


W, H = 1920, 1080
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Rookie2_main.png"
OUT = ROOT / "Concept"

TITLE_FULL = ["ROOKIE2", "Autonomy at Scale"]
TITLE_SHORT = ["ROOKIE2"]
SUB_LINES = [
    "Scaling autonomous delivery across real-world buildings,",
    "one seamless journey at a time.",
]

FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_BLACK = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
FONT_MONO = "/System/Library/Fonts/SFNSMono.ttf"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


def cover(img: Image.Image, zoom: float = 1.0, ox: float = 0.0, oy: float = 0.0) -> Image.Image:
    scale = max(W / img.width, H / img.height) * zoom
    nw, nh = round(img.width * scale), round(img.height * scale)
    resized = img.resize((nw, nh), Image.Resampling.LANCZOS)
    left = round(max(0, nw - W) * (0.5 + ox * 0.5))
    top = round(max(0, nh - H) * (0.5 + oy * 0.5))
    return resized.crop((left, top, left + W, top + H)).convert("RGBA")


def overlay(img: Image.Image, color: tuple[int, int, int], alpha: int) -> Image.Image:
    return Image.alpha_composite(img.convert("RGBA"), Image.new("RGBA", (W, H), (*color, alpha)))


def gradient(start: tuple[int, int, int, int], end: tuple[int, int, int, int], vertical: bool = True) -> Image.Image:
    out = Image.new("RGBA", (W, H))
    d = ImageDraw.Draw(out)
    steps = H if vertical else W
    for i in range(steps):
        t = i / max(1, steps - 1)
        color = tuple(round(start[j] * (1 - t) + end[j] * t) for j in range(4))
        if vertical:
            d.line((0, i, W, i), fill=color)
        else:
            d.line((i, 0, i, H), fill=color)
    return out


def layer() -> Image.Image:
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def text_wh(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, stroke_width: int = 0) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt, stroke_width=stroke_width)
    return box[2] - box[0], box[3] - box[1]


def draw_title(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    lines: list[str],
    size: int,
    fill: tuple[int, int, int, int],
    anchor: str = "la",
    align: str = "left",
    leading: float = 1.04,
    stroke: tuple[int, int, int, int] | None = None,
    stroke_width: int = 0,
) -> None:
    # Title lines intentionally share the same size and weight.
    fnt = font(FONT_BLACK, size)
    x, y = xy
    heights = [text_wh(draw, line, fnt, stroke_width)[1] for line in lines]
    total_h = round(sum(heights) + (len(lines) - 1) * size * (leading - 0.72))
    if anchor.startswith("m"):
        y -= total_h // 2
    for line in lines:
        tw, th = text_wh(draw, line, fnt, stroke_width)
        tx = x
        if align == "center":
            tx = x - tw // 2
        elif align == "right":
            tx = x - tw
        draw.text(
            (tx, y),
            line,
            font=fnt,
            fill=fill,
            stroke_width=stroke_width,
            stroke_fill=stroke or fill,
        )
        y += round(size * leading)


def draw_subtitle(draw: ImageDraw.ImageDraw, xy: tuple[int, int], fill: tuple[int, int, int, int], size: int = 30, align: str = "left") -> None:
    fnt = font(FONT_BOLD, size)
    x, y = xy
    for line in SUB_LINES:
        tx = x
        if align == "center":
            tx = x - text_wh(draw, line, fnt)[0] // 2
        elif align == "right":
            tx = x - text_wh(draw, line, fnt)[0]
        draw.text((tx, y), line, font=fnt, fill=fill)
        y += round(size * 1.2)


def draw_arrow(draw: ImageDraw.ImageDraw, dark: bool = False) -> None:
    bg = (255, 255, 255, 245) if not dark else (8, 10, 12, 235)
    fg = (0, 0, 0, 235) if not dark else (255, 255, 255, 235)
    x, y, s = 1845, 40, 38
    draw.rectangle((x, y, x + s, y + s), fill=bg, outline=fg, width=2)
    draw.line((x + 11, y + 15, x + 19, y + 23, x + 27, y + 15), fill=fg, width=3)


def draw_plus(draw: ImageDraw.ImageDraw, xy: tuple[int, int], size: int = 92, fill: tuple[int, int, int, int] = (255, 255, 255, 190)) -> None:
    x, y = xy
    draw.line((x, y + size // 2, x + size // 2, y + size // 2), fill=fill, width=2)
    draw.line((x + size // 4, y + size // 4, x + size // 4, y + size * 3 // 4), fill=fill, width=2)
    draw.line((x + size * 3 // 5, y + size // 5, x + size, y + size * 4 // 5), fill=fill, width=2)
    draw.line((x + size, y + size // 5, x + size * 3 // 5, y + size * 4 // 5), fill=fill, width=2)


def crop_object(base: Image.Image, zoom: float = 1.0) -> Image.Image:
    """Soft rectangular product crop used as a reusable hero object."""
    obj = cover(base, zoom=zoom, ox=0.05, oy=0.0)
    mask = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(mask)
    poly = [(390, 135), (855, 100), (1515, 250), (1535, 1080), (360, 1080)]
    d.polygon(poly, fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(10))
    obj.putalpha(mask)
    return obj


def save(img: Image.Image, filename: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(OUT / filename, "PNG", optimize=True)


def c01_top_information(base: Image.Image) -> Image.Image:
    img = cover(base, zoom=1.48, ox=-0.5, oy=-0.1)
    img = ImageEnhance.Color(img).enhance(0.32)
    img = ImageEnhance.Contrast(img).enhance(1.06)
    img = overlay(img, (196, 177, 148), 72)
    img = Image.alpha_composite(img, gradient((0, 0, 0, 90), (0, 0, 0, 8), vertical=True))
    d = ImageDraw.Draw(img)
    white = (255, 255, 255, 238)
    pink = (255, 183, 177, 238)
    draw_title(d, (58, 84), ["ROOKIE2", "AUTONOMY AT SCALE"], 32, white)
    d.text((60, 172), "AUTONOMOUS DELIVERY PLATFORM", font=font(FONT_BOLD, 15), fill=white)
    d.text((60, 210), "ROOKIE2", font=font(FONT_BOLD, 15), fill=white)
    draw_subtitle(d, (60, 238), white, 15)
    draw_title(d, (W // 2, 86), ["ROOKIE2", "UXUI RENEWAL"], 32, white, align="center")
    d.text((W // 2, 216), "REAL-WORLD BUILDING EXPERIENCE", font=font(FONT_BOLD, 15), fill=white, anchor="ma")
    d.text((W - 235, 84), "PLUS X\nCREATIVE PARTNER", font=font(FONT_BLACK, 28), fill=white, anchor="ra", align="right")
    d.text((W - 235, 205), "Integrated service design for\nrobot delivery operations.", font=font(FONT_BOLD, 15), fill=pink, anchor="ra", align="right")
    draw_arrow(d)
    return img


def c02_bottom_credits(base: Image.Image) -> Image.Image:
    bg = Image.new("RGBA", (W, H), (222, 230, 234, 255))
    soft = cover(base, zoom=1.02)
    soft = ImageEnhance.Brightness(soft).enhance(1.25)
    soft = ImageEnhance.Contrast(soft).enhance(0.72)
    soft = ImageEnhance.Color(soft).enhance(0.42)
    bg = Image.alpha_composite(bg, soft.putalpha(88) or soft)
    obj = crop_object(Image.open(SOURCE).convert("RGB"), zoom=1.02)
    obj = ImageEnhance.Brightness(obj).enhance(1.16)
    obj = ImageEnhance.Contrast(obj).enhance(0.92)
    bg = Image.alpha_composite(bg, obj)
    d = ImageDraw.Draw(bg)
    dark_blue = (43, 50, 70, 235)
    draw_title(d, (W // 2, 390), TITLE_SHORT, 74, dark_blue, align="center")
    d.text((W // 2, 478), "Autonomy at Scale", font=font(FONT_BLACK, 74), fill=dark_blue, anchor="ma")
    draw_arrow(d)
    credits = [
        ("PROJECT", "Building delivery UX/UI\nOperational route design\nRobot service experience"),
        ("CREATIVE DIRECTOR", "ROOKIE2 Studio\nAutonomy Systems"),
        ("BX STRATEGY", "Real-world logistics\nService architecture"),
        ("UX DESIGNER", "Fleet dashboard\nJourney mapping"),
        ("UI DESIGNER", "Interface design\nMotion language"),
    ]
    x = 64
    for head, body in credits:
        d.text((x, 872), head, font=font(FONT_BLACK, 18), fill=(255, 255, 255, 232))
        d.multiline_text((x, 910), body, font=font(FONT_BOLD, 18), fill=(255, 255, 255, 218), spacing=8)
        x += 285 if head != "UI DESIGNER" else 0
    draw_plus(d, (1740, 878), 90, (255, 255, 255, 180))
    d.text((1680, 1012), "© 2026 ROOKIE2 Creative Partner.", font=font(FONT_BOLD, 16), fill=(255, 255, 255, 210))
    return bg


def c03_dark_device(base: Image.Image) -> Image.Image:
    img = cover(base, zoom=1.3, ox=0.1, oy=-0.02)
    img = ImageEnhance.Color(img).enhance(0.48)
    img = ImageEnhance.Contrast(img).enhance(1.18)
    img = overlay(img, (15, 23, 32), 86)
    img = Image.alpha_composite(img, gradient((5, 7, 10, 170), (5, 7, 10, 20), vertical=False))
    d = ImageDraw.Draw(img)
    draw_title(d, (405, -26), ["ROOKIE2", "AUTONOMY", "AT SCALE"], 76, (255, 255, 255, 238))
    draw_subtitle(d, (410, 258), (255, 255, 255, 230), 18)
    draw_plus(d, (1372, 0), 92, (255, 255, 255, 160))
    draw_arrow(d)
    d.rounded_rectangle((1798, 1038, 1878, 1056), radius=2, fill=(255, 255, 255, 245))
    d.text((1810, 1041), "SHARE THIS", font=font(FONT_BLACK, 9), fill=(15, 20, 24, 235))
    return img


def c04_center_logo(base: Image.Image) -> Image.Image:
    img = cover(base, zoom=1.36, ox=-0.12, oy=0.18)
    img = ImageEnhance.Color(img).enhance(0.34)
    img = ImageEnhance.Contrast(img).enhance(1.2)
    img = overlay(img, (77, 54, 38), 118)
    d = ImageDraw.Draw(img)
    rose = (255, 167, 160, 238)
    white = (255, 255, 255, 245)
    d.text((W // 2, 154), "That’s So you, Rookie2", font=font(FONT_BLACK, 22), fill=rose, anchor="ma")
    d.text((W // 2, 190), "PC & Mobile Web UX/UI eXperience Design", font=font(FONT_BLACK, 23), fill=rose, anchor="ma")
    draw_title(d, (W // 2, 520), TITLE_SHORT, 150, white, align="center", anchor="ma")
    d.text((W // 2, 938), "© 2026 Plus X Co.", font=font(FONT_BLACK, 20), fill=rose, anchor="ma")
    draw_arrow(d)
    d.rounded_rectangle((1798, 1038, 1878, 1056), radius=2, fill=(255, 255, 255, 245))
    d.text((1810, 1041), "SHARE THIS", font=font(FONT_BLACK, 9), fill=(15, 20, 24, 235))
    return img


def c05_blue_overlay(base: Image.Image) -> Image.Image:
    img = cover(base, zoom=1.2, ox=0.03, oy=0.0)
    img = ImageEnhance.Color(img).enhance(0.24)
    img = ImageEnhance.Brightness(img).enhance(1.15)
    img = overlay(img, (35, 106, 238), 190)
    img = Image.alpha_composite(img, gradient((240, 247, 255, 86), (35, 106, 238, 70), vertical=True))
    d = ImageDraw.Draw(img)
    white = (255, 255, 255, 248)
    blue = (34, 105, 234, 255)
    d.rounded_rectangle((W // 2 - 145, H // 2 - 62, W // 2 + 145, H // 2 + 62), radius=62, fill=white)
    d.text((W // 2, H // 2 - 39), "Rookie2", font=font(FONT_BLACK, 54), fill=blue, anchor="ma")
    draw_title(d, (84, 855), ["ROOKIE2", "Brand eXperience", "Renewal Project"], 46, white)
    draw_subtitle(d, (84, 1010), white, 17)
    d.text((1545, 994), "© 2026 Plus X Co.Ltd. All Rights Reserved.", font=font(FONT_BLACK, 16), fill=white)
    draw_arrow(d)
    d.rounded_rectangle((1798, 1038, 1878, 1056), radius=2, fill=white)
    d.text((1810, 1041), "SHARE THIS", font=font(FONT_BLACK, 9), fill=blue)
    return img


def c06_rules_editorial(base: Image.Image) -> Image.Image:
    bg = Image.new("RGBA", (W, H), (178, 192, 214, 255))
    obj = crop_object(base, zoom=1.05)
    obj = ImageEnhance.Brightness(obj).enhance(1.25)
    obj = ImageEnhance.Contrast(obj).enhance(0.8)
    obj = obj.resize((round(W * 0.96), H), Image.Resampling.LANCZOS)
    bg.alpha_composite(obj, (260, 0))
    d = ImageDraw.Draw(bg)
    white = (255, 255, 255, 245)
    for y in [86, 500, 920]:
        d.rectangle((150, y, 1760, y + 14), fill=white)
    draw_title(d, (154, 148), ["ROOKIE2 BRAND", "EXPERIENCE DESIGN"], 78, white)
    draw_plus(d, (1580, 148), 92, (255, 255, 255, 165))
    d.text((154, 555), "PLUS X", font=font(FONT_BLACK, 15), fill=white)
    d.multiline_text((154, 610), "CREATIVE DIRECTOR\nROOKIE2 STUDIO\n\nBX STRATEGY\nAUTONOMY SYSTEMS\n\nPRODUCT DESIGNER\nSERVICE ROBOTICS", font=font(FONT_BLACK, 15), fill=white, spacing=7)
    d.multiline_text((360, 610), "UX DESIGNER\nREAL-WORLD ROUTES\nBUILDING JOURNEYS\n\nUI DESIGNER\nCONTROL INTERFACES\n\nDEVELOPER\nSCALE PLATFORM", font=font(FONT_BLACK, 15), fill=white, spacing=7)
    d.multiline_text((600, 610), "AUTONOMOUS DELIVERY\nREAL-WORLD BUILDINGS\n\nONE SEAMLESS JOURNEY\nAT A TIME.", font=font(FONT_BLACK, 15), fill=white, spacing=7)
    d.text((1645, 558), "© 2026 ROOKIE2 Co. Ltd.", font=font(FONT_BLACK, 15), fill=white)
    draw_arrow(d)
    d.rounded_rectangle((1798, 1038, 1878, 1056), radius=2, fill=white)
    d.text((1810, 1041), "SHARE THIS", font=font(FONT_BLACK, 9), fill=(40, 50, 62, 240))
    return bg


def c07_centered_space(base: Image.Image) -> Image.Image:
    img = cover(base, zoom=1.0, ox=0, oy=-0.15)
    img = ImageEnhance.Brightness(img).enhance(1.38)
    img = ImageEnhance.Contrast(img).enhance(0.58)
    img = ImageEnhance.Color(img).enhance(0.45)
    img = overlay(img, (207, 211, 235), 150)
    fade = gradient((207, 211, 235, 80), (207, 211, 235, 10), vertical=True)
    img = Image.alpha_composite(img, fade)
    d = ImageDraw.Draw(img)
    white = (255, 255, 255, 245)
    d.multiline_text((36, 40), "PlusX\nCreative Director : ROOKIE2 Studio\nStrategy Director : Autonomy Ops\nBX Strategist : Building Delivery", font=font(FONT_BLACK, 15), fill=white, spacing=5)
    d.multiline_text((310, 40), "Group ROOKIE2\nCEO : Scale Platform\nProject TF : Robot UX, Fleet Ops,\nReal-world Journey", font=font(FONT_BLACK, 15), fill=white, spacing=5)
    d.text((W // 2, 43), "© 2026 ROOKIE2 Co. Ltd. All Right Reserved", font=font(FONT_BLACK, 15), fill=white, anchor="ma")
    draw_plus(d, (1665, 40), 112, (255, 255, 255, 170))
    draw_title(d, (W // 2, 515), ["ROOKIE2", "Brand eXperience", "Design"], 62, white, align="center", anchor="ma")
    draw_subtitle(d, (W // 2, 650), white, 18, align="center")
    d.polygon([(W // 2, 1015), (W // 2 - 30, 1080), (W // 2 + 30, 1080)], fill=white)
    draw_arrow(d)
    d.rounded_rectangle((1798, 1038, 1878, 1056), radius=2, fill=white)
    d.text((1810, 1041), "SHARE THIS", font=font(FONT_BLACK, 9), fill=(40, 50, 62, 240))
    return img


def main() -> None:
    base = Image.open(SOURCE).convert("RGB")
    OUT.mkdir(parents=True, exist_ok=True)
    for existing in OUT.glob("*.png"):
        existing.unlink()

    concepts = [
        ("01_ref_top_information.png", c01_top_information),
        ("02_ref_bottom_credits.png", c02_bottom_credits),
        ("03_ref_dark_device.png", c03_dark_device),
        ("04_ref_center_logo.png", c04_center_logo),
        ("05_ref_blue_overlay.png", c05_blue_overlay),
        ("06_ref_rules_editorial.png", c06_rules_editorial),
        ("07_ref_centered_space.png", c07_centered_space),
    ]
    for filename, renderer in concepts:
        save(renderer(base.copy()), filename)
        print(OUT / filename)


if __name__ == "__main__":
    main()
