import sys
import os
from PIL import Image

def opacify(src, color=(255, 255, 255), dest=None):
    dest = dest or src
    for file in os.listdir(src):
        if file.lower().endswith(".png"):
            path = os.path.join(src, file)
            img = Image.open(path).convert("RGBA")
            bg = Image.new("RGB", img.size, color)
            bg.paste(img, mask=img.getchannel("A"))
            bg.save(os.path.join(dest, file))

if __name__ == "__main__":
    src = sys.argv[1]
    color = (255, 255, 255) if len(sys.argv) < 3 or sys.argv[2] in ("white", "w") else (0, 0, 0)
    dest = sys.argv[3] if len(sys.argv) > 3 else None
    opacify(src, color, dest)
