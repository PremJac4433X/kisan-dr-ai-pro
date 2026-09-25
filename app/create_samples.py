"""
Utility to generate synthetic realistic plant pathology sample images
for immediate testing and demo purposes in static/samples/.
"""

import os
import math
import random
from PIL import Image, ImageDraw, ImageFilter

def create_sample_leaves(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    random.seed(42)

    # 1. Healthy Tomato Leaf
    img_h = Image.new("RGB", (320, 320), (242, 246, 240))
    draw = ImageDraw.Draw(img_h)
    # Draw leaf silhouette
    draw.polygon([(160, 40), (250, 100), (260, 200), (200, 260), (160, 290), (120, 260), (60, 200), (70, 100)], fill=(46, 125, 50))
    # Veins
    draw.line([(160, 40), (160, 290)], fill=(76, 175, 80), width=4)
    for y in range(80, 260, 30):
        draw.line([(160, y), (160 + int((y-40)*0.4), y - 15)], fill=(76, 175, 80), width=2)
        draw.line([(160, y), (160 - int((y-40)*0.4), y - 15)], fill=(76, 175, 80), width=2)
    img_h = img_h.filter(ImageFilter.GaussianBlur(1.0))
    img_h.save(os.path.join(output_dir, "tomato_healthy.jpg"), quality=90)

    # 2. Tomato Early Blight (Concentric target board rings + yellow halos)
    img_eb = Image.new("RGB", (320, 320), (242, 246, 240))
    draw = ImageDraw.Draw(img_eb)
    draw.polygon([(160, 40), (250, 100), (260, 200), (200, 260), (160, 290), (120, 260), (60, 200), (70, 100)], fill=(56, 115, 45))
    draw.line([(160, 40), (160, 290)], fill=(76, 155, 60), width=4)
    # Draw chlorotic yellow patches
    draw.ellipse([110, 110, 180, 180], fill=(210, 190, 40))
    draw.ellipse([180, 180, 240, 240], fill=(215, 195, 45))
    # Draw necrotic dark brown concentric rings
    for r in range(25, 5, -5):
        draw.ellipse([145 - r, 145 - r, 145 + r, 145 + r], outline=(70, 40, 20), width=2)
    draw.ellipse([140, 140, 150, 150], fill=(50, 25, 10))
    for r in range(20, 5, -5):
        draw.ellipse([210 - r, 210 - r, 210 + r, 210 + r], outline=(65, 35, 18), width=2)
    draw.ellipse([207, 207, 213, 213], fill=(50, 25, 10))
    img_eb = img_eb.filter(ImageFilter.GaussianBlur(1.0))
    img_eb.save(os.path.join(output_dir, "tomato_early_blight.jpg"), quality=90)

    # 3. Potato Late Blight (Dark water-soaked expanding patches)
    img_lb = Image.new("RGB", (320, 320), (242, 246, 240))
    draw = ImageDraw.Draw(img_lb)
    draw.polygon([(160, 35), (260, 95), (255, 210), (190, 270), (160, 295), (130, 270), (65, 210), (60, 95)], fill=(45, 105, 40))
    # Dark black-brown water soaked margins
    draw.polygon([(160, 35), (260, 95), (230, 150), (160, 110)], fill=(30, 25, 20))
    draw.polygon([(65, 210), (120, 230), (130, 270), (70, 260)], fill=(35, 30, 22))
    # Greyish pale margin halo
    draw.line([(230, 150), (160, 110)], fill=(160, 170, 140), width=3)
    img_lb = img_lb.filter(ImageFilter.GaussianBlur(1.2))
    img_lb.save(os.path.join(output_dir, "potato_late_blight.jpg"), quality=90)

    # 4. Rice Blast (Spindle/diamond-shaped lesions)
    img_rb = Image.new("RGB", (320, 320), (242, 246, 240))
    draw = ImageDraw.Draw(img_rb)
    # Long slender paddy leaf
    draw.polygon([(160, 20), (195, 140), (190, 290), (160, 310), (130, 290), (125, 140)], fill=(60, 130, 50))
    draw.line([(160, 20), (160, 310)], fill=(80, 160, 70), width=3)
    # Spindle lesions
    def draw_spindle(cx, cy, rx, ry):
        draw.polygon([(cx, cy - ry), (cx + rx, cy), (cx, cy + ry), (cx - rx, cy)], fill=(139, 69, 19))
        draw.polygon([(cx, cy - int(ry*0.6)), (cx + int(rx*0.6), cy), (cx, cy + int(ry*0.6)), (cx - int(rx*0.6), cy)], fill=(200, 200, 200))
    draw_spindle(160, 110, 15, 35)
    draw_spindle(145, 190, 12, 28)
    draw_spindle(170, 240, 10, 22)
    img_rb = img_rb.filter(ImageFilter.GaussianBlur(1.0))
    img_rb.save(os.path.join(output_dir, "rice_blast.jpg"), quality=90)

    # 5. Corn Common Rust (Rusty orange-brown pustules)
    img_cr = Image.new("RGB", (320, 320), (242, 246, 240))
    draw = ImageDraw.Draw(img_cr)
    # Wide corn leaf
    draw.polygon([(160, 25), (230, 120), (220, 280), (160, 305), (100, 280), (90, 120)], fill=(70, 140, 55))
    draw.line([(160, 25), (160, 305)], fill=(95, 175, 75), width=5)
    # Rusty pustules
    for _ in range(45):
        px = random.randint(110, 210)
        py = random.randint(60, 270)
        draw.ellipse([px-4, py-2, px+4, py+2], fill=(185, 75, 15))
        draw.ellipse([px-2, py-1, px+2, py+1], fill=(225, 105, 25))
    img_cr = img_cr.filter(ImageFilter.GaussianBlur(0.8))
    img_cr.save(os.path.join(output_dir, "corn_rust.jpg"), quality=90)

    # 6. Cotton Bacterial Blight (Angular leaf spot)
    img_cb = Image.new("RGB", (320, 320), (242, 246, 240))
    draw = ImageDraw.Draw(img_cb)
    # Cotton palmate leaf lobes
    draw.polygon([(160, 50), (230, 80), (260, 160), (210, 210), (160, 280), (110, 210), (60, 160), (90, 80)], fill=(50, 120, 60))
    # Veins
    draw.line([(160, 280), (160, 50)], fill=(70, 150, 80), width=3)
    draw.line([(160, 200), (230, 80)], fill=(70, 150, 80), width=3)
    draw.line([(160, 200), (90, 80)], fill=(70, 150, 80), width=3)
    # Angular dark necrotic spots bounded by veins
    angular_spots = [
        [(150, 110), (170, 115), (165, 135), (145, 130)],
        [(180, 140), (200, 145), (195, 165), (175, 160)],
        [(120, 150), (140, 155), (135, 175), (115, 170)],
        [(160, 170), (175, 175), (170, 195), (155, 190)]
    ]
    for spot in angular_spots:
        draw.polygon(spot, fill=(60, 20, 15))
    img_cb = img_cb.filter(ImageFilter.GaussianBlur(1.0))
    img_cb.save(os.path.join(output_dir, "cotton_blight.jpg"), quality=90)
    print("Generated 6 synthetic realistic leaf diagnostic samples in:", output_dir)

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "..", "static", "samples")
    create_sample_leaves(out)
