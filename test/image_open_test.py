from PIL import Image

image_11 = "https://2019.images.forbesjapan.media/articles/28000/28737/photos/410x615/287372b32bafc0a65daabbbb31509e5349859.jpg"
img = Image.open(image_11)
# For each face returned use the face rectangle and draw a red box.
print('Drawing rectangle around face... see popup for results.')

# draw = ImageDraw.Draw(img)
# draw.rectangle(getRectangle_ver2(array_11), outline='red')

# Display the image in the default image browser.
img.show()
