from PIL import Image
import ctypes

width = 2048
height = 2048
img = Image.new("RGB", (width, height))

x = int(width/2)
y = int(height/2)

with open("packets.txt") as f:
    for line in f:
        bytes = f.readline().strip()[2:-4]
        click = int(ctypes.c_int8(int(bytes[0:2], 16)).value)
        x_dis = int(ctypes.c_int8(int(bytes[2:4], 16)).value)
        y_dis = int(ctypes.c_int8(int(bytes[4:6], 16)).value)

        x += x_dis
        y += y_dis

        if click:
                img.putpixel((x, y), (255, 0, 0))

img.save("image.png")
