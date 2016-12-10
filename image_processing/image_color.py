from PIL import Image

for i in range(200):
    img = Image.open("images/image{}.png".format(i))
    img = img.convert("RGB")
    pixdata = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if sum(pixdata[x, y]) >= 250 or pixdata[x, y][0] >= 128:
                pixdata[x, y] = (255, 255, 255)
    img.save('processed/image{}.png'.format(i))
    print("image {} processed".format(i))
