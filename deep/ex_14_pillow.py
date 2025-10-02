from PIL import Image

smileman = Image.open("C:/Users/USER/Desktop/hancom/python/deep/assets/new_smileman.png")
smileman.size
(101, 80)
smileman = smileman.crop((15, 10, 80, 75))
smileman.save("C:/Users/USER/Desktop/hancom/python/deep/assets/smileman.png", "png")