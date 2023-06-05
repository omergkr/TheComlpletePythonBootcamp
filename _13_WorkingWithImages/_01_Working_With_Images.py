from PIL import Image

computer_image = Image.open("my_computer_image.jpg")
print(type(computer_image))
print(computer_image.size)

# Cropping images

cam = computer_image.crop((0, 0, 100, 100))
computer_image.paste(im=cam, box=(0, 0))
print(type(cam))
print(cam.size)

resized = computer_image.resize((300, 500))
resized.save("resized.jpg")
print(computer_image.size)
rotated = computer_image.rotate(90)
rotated.save("rotated.jpg")

# Color Transparency
# RGBA red green blue alpha
blue = Image.open("blue_color.png")
red = Image.open("red_color.jpg")

blue.paste(im=red, box=(0, 0), mask=red)

blue.save("purple.png")

purple = Image.open("purple.png")
